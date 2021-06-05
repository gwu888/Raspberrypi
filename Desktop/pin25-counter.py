# http://raspberrypi-aa.github.io/session2/input.html
# Pin 25 pulse counter

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # set GPIO25 as input, and PUD_DOWN

pulse_count = 0

def callback_function_pulse_counter(input_pin): 
  global pulse_count
  pulse_count = pulse_count + 1
  print("Input on pin", input_pin, "Count = ", pulse_count)

GPIO.add_event_detect(25, GPIO.RISING, callback=callback_function_pulse_counter)
while True:
    1==1

GPIO.cleanup()         # clean up before use
