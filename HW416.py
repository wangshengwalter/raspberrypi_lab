import RPi.GPIO as GPIO
import time
 
PIR_input = 8   #read PIR Output
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
