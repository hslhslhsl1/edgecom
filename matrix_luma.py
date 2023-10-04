import numpy as np
from PIL import Image
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop

def matrix_display(device, matrix):
    """Display a 2D numpy array on the LED matrix.
    This is a wrapper function that converts a 2D numpy
    matrix into a 1-bit B/W image and then displays it
    on the LED matrix.
    
    Parameters
    ----------
    device : luma.led_matrix.device.max7219
        A Luma LED matrix device object.
    matrix: uint8 numpy.ndarray
        A 2D binary numpy array.
        
    """
    # Convert "1" values in binary matrix to 255
    matrix_g = np.where(matrix==1, 255, matrix)

    # Creating a 1-bit B/W image directly from a binary
    # numpy array does not work for some reason (maybe
    # a bug in Pillow).
    # Create greyscale PIL image from a 2D numpy array
    image_g = Image.fromarray(matrix_g, mode='L')
    
    # Convert greyscale image to 1-bit B/W
    image_bw = image_g.convert('1')
    
    # Display image on LED matrix
    device.display(image_bw)
    

def matrix_display8(device, matrix):
    """Display 1 8x8 matrix twice as 8x16
    Convenience function to display the same image
    on both 8x8 LED matrices.
    
    Parameters
    ----------
    device : luma.led_matrix.device.max7219
        A Luma LED matrix device object.
    matrix: uint8 numpy.ndarray
        An 8x8 2D binary numpy array.
     
    """
    # Copy the 8x8 matrix into an 8x16 matrix
    matrix16 = np.hstack([matrix, matrix])
    
    # Display on LED matrix
    matrix_display(device, matrix16)


if __name__ == '__main__':
    # create LED matrix device 
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, height=8, width=16, rotate=0, block_orientation=90)
    
    # Clear display
    device.clear()
    
    # Set LED brightness (int 0-255)
    device.contrast(255)
    
    # Example displays
    happy = np.array(
    [[0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0],
     [0,0,0,1,1,0,0,0,    0,0,0,1,1,0,0,0],
     [0,0,1,0,0,1,0,0,    0,0,1,0,0,1,0,0],
     [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,    0,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,1,    1,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0]
    ],
    dtype='uint8')
    
    eye = np.array(
    [[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,1,1,0,0,0],
     [0,0,0,1,1,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]
    ],
    dtype='uint8')
    
    hs = np.array(
    [[0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0],
     [0,1,0,0,0,0,1,0,    0,1,1,1,1,1,1,0],
     [0,1,0,0,0,0,1,0,    0,1,0,0,0,0,0,0],
     [0,1,1,1,1,1,1,0,    0,1,0,0,0,0,0,0],
     [0,1,0,0,0,0,1,0,    0,1,1,1,1,1,1,0],
     [0,1,0,0,0,0,1,0,    0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,1,0,    0,1,1,1,1,1,1,0],
     [0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0]
    ],
    dtype='uint8')
    
    #matrix_display(device, happy)
    #matrix_display8(device, eye)
    #matrix_display(device,hs) 