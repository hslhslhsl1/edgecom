import  RPi.GPIO as GPIO
import time
import sys


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.OUT)


try:
   
    
    while True:
            print("Button is clicked!")
            GPIO.output(14,0)
            time.sleep(1)
            GPIO.output(14,1)
            time.sleep(1)


                
except  KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup() 