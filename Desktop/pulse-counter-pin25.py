# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
# Problem: the Pin 25 detects both Rising and Falling, double counted.

from datetime import datetime
from time import sleep     # this lets us have a time delay (see line 15)
import numpy as np
import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
# set GPIO25 as input, and PUD_DOWN
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.OUT)   # set GPIO24 as an output-pin (LED)

gpio25_counter_lifetime_file = '/home/pi/data/gpio25-counter-lifetime.txt'
gpio25_counter_monthly_file  = '/home/pi/data/gpio25-counter-monthly.txt'

GPIO.output(24, 0)         # set LED=OFF as initial state
total_pulse_count = 0
last_reading_count = 0

def callback_function_pulse_counter(input_pin): 
  global total_pulse_count
  global last_reading_count
  total_pulse_count = total_pulse_count + 1
  print("Input on pin", input_pin, "Count = ", total_pulse_count)
  state = GPIO.input(24)
  if state:
  #print('Turn LED off...')
      GPIO.output(24, 0)
  else: 
      #print('Turn LED On...')
      GPIO.output(24, 1)

# Forever loop wait for event detected then run callback:
GPIO.add_event_detect(25, GPIO.RISING, callback=callback_function_pulse_counter)

# print total_pulse_count
def print_total_pulse_hourly():
    while True:
        global total_pulse_count
        fopen_life = open(gpio25_counter_lifetime_file, 'a+')
        fopen_life.write("%s,%d\n" % (datetime.now(),total_pulse_count))
        fopen_life.close()
        sleep(3600)

def print_pulse_5_minutes():
    while True:            # this will carry on until you hit CTRL+C
        global total_pulse_count
        global last_reading_count
        # get this usage count
        this_usage_count = total_pulse_count - last_reading_count
        last_reading_count = total_pulse_count 			# remember last reading
        #print(datetime.now(),",",this_usage_count)
        fopen_month = open(gpio25_counter_monthly_file, 'a+')
        fopen_month.write("%s,%d\n" % (datetime.now(),this_usage_count))
        fopen_month.close()
        sleep(60)

thread1 = threading.Thread(target=print_total_pulse_hourly)
thread1.start()

thread2 = threading.Thread(target=print_pulse_5_minutes)
thread2.start()

while True:
    1==1

GPIO.cleanup()         # clean up after yourself
