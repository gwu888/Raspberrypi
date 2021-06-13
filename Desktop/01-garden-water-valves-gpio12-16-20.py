import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT) # valve1
GPIO.setup(16, GPIO.OUT) # valve2
GPIO.setup(20, GPIO.OUT) # valve3
GPIO.setup(21, GPIO.OUT) # valve3

GPIO.output(12, GPIO.HIGH)
print("Sleep 60 seconds for GPIO12=high")
time.sleep(60)

GPIO.output(12, GPIO.LOW)
print("Sleep 10 seconds for GPIO12=low")
time.sleep(10)

GPIO.output(16, GPIO.HIGH)
print("Sleep 60 seconds for GPIO16=high")
time.sleep(60)

GPIO.output(16, GPIO.LOW)
print("Sleep 10 seconds for GPIO16=low")
time.sleep(10)

GPIO.output(20, GPIO.HIGH)
print("Sleep 60 seconds for GPIO20=high")
time.sleep(60)

GPIO.output(20, GPIO.LOW)
print("Sleep 10 seconds for GPIO20=low")
time.sleep(10)

GPIO.output(21, GPIO.HIGH)
print("Sleep 60 seconds for GPIO21=high")
time.sleep(60)

GPIO.output(21, GPIO.LOW)
print("Sleep 10 seconds for GPIO21=low")

time.sleep(10)

GPIO.cleanup()

