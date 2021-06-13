import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

GPIO.output(25, GPIO.HIGH)
print("Sleep 10 seconds for GPIO25=high")
time.sleep(10)

GPIO.output(25, GPIO.LOW)
print("Sleep 10 seconds for GPIO25=low")
time.sleep(10)

GPIO.output(25, GPIO.HIGH)
print("Sleep 10 seconds for GPIO25=high")
time.sleep(10)

GPIO.output(25, GPIO.LOW)
print("Sleep 10 seconds for GPIO25=low")
time.sleep(10)

GPIO.cleanup()

