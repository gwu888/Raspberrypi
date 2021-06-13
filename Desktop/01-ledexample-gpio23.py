import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)
print("Sleep 10 seconds for GPIO23=high")
time.sleep(10)

GPIO.output(23, GPIO.LOW)
print("Sleep 10 seconds for GPIO23=low")
time.sleep(10)

GPIO.output(23, GPIO.HIGH)
print("Sleep 10 seconds for GPIO23=high")
time.sleep(10)

GPIO.output(23, GPIO.LOW)
print("Sleep 10 seconds for GPIO23=low")
time.sleep(10)

GPIO.cleanup()

