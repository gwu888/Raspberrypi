import RPi.GPIO as GPIO
import time

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    
    GPIO.output(25, GPIO.HIGH)
    print("Sleep 3 seconds for GPIO25=high")
    time.sleep(3)
    
    GPIO.output(25, GPIO.LOW)
    print("Sleep 3 seconds for GPIO25=low")
    time.sleep(3)

GPIO.cleanup()

