import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

GPIO.output(24, GPIO.HIGH)
print("Sleep 10 seconds for GPIO24=high")
time.sleep(10)

GPIO.output(24, GPIO.LOW)
print("Sleep 10 seconds for GPIO24=low")
time.sleep(10)

GPIO.output(24, GPIO.HIGH)
print("Sleep 10 seconds for GPIO24=high")
time.sleep(10)

GPIO.output(24, GPIO.LOW)
print("Sleep 10 seconds for GPIO24=low")
time.sleep(10)

GPIO.output(24, GPIO.HIGH)
print("Sleep 10 seconds for GPIO24=high")
time.sleep(10)

GPIO.output(24, GPIO.LOW)
print("Sleep 10 seconds for GPIO24=low")
time.sleep(10)

GPIO.cleanup()

