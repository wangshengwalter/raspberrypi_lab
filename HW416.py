import RPi.GPIO as GPIO
import time
#see from back side(no ball side)
#first one->5v
#second one->16(physic pin)
#third GND->GND
 
PIR_input = 16   #read PIR Output
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)
 
while True:
    if GPIO.input(PIR_input):
        
        print('Input was HIGH')
    else:
        print('Input was LOW')
        
    time.sleep(0.5)
GPIO.cleanup()
