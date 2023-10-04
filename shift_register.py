import RPi.GPIO as GPIO
import sys
import time

dataPIN = 16
latchPIN = 20
clockPIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup((dataPIN,latchPIN,clockPIN),GPIO.OUT)




def shift_update(input,data,clock,latch):
    
    GPIO.output(clock,0)
    GPIO.output(latch,0)
    GPIO.output(clock,1)
    
    for i in range(7,-1,-1):
        GPIO.output(clock,0)
        GPIO.output(data,int(input[i]))
        GPIO.output(clock,1)
        
    GPIO.output(clock,0)
    GPIO.output(latch,1)
    GPIO.output(clock,1)

try:

    while True:
        
        ttt = GPIO.input(12)
        # print(ttt)
        

        if ttt == False:    
            print("Button is clicked")
            temp = '10101010'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '11010101'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '10101010'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '11010101'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '11010101'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '11010101'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '10101010'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '11010101'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '10101010'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '11111111'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '11010101'
            shift_update(temp,dataPIN,clockPIN,latchPIN)
            time.sleep(0.3)
            temp = '00000000'
            shift_update(temp,dataPIN,clockPIN,latchPIN)

except  KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
 


