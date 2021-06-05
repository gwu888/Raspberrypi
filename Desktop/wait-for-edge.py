# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
#
import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set GPIO25 as input (button)  
GPIO.setup(24, GPIO.OUT)   # set GPIO24 as an output (LED)  

x = 0  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        GPIO.wait_for_edge(25, GPIO.RISING)
    	x = x + 1
        print "Port 25 is 1/HIGH/True - LED ON," 
        print (x)
        GPIO.output(24, 0)         # set port/pin value to 1/HIGH/True  
	GPIO.wait_for_edge(25, GPIO.FALLING)
        print "Port 25 is 0/LOW/False - LED OFF"  
        GPIO.output(24, 1)         # set port/pin value to 0/LOW/False  
        sleep(0.1)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
