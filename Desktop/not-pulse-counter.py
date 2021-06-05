#!/usr/bin/python

import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

workfile = '/home/pi/data/gpio25-counter'
counter = 0

while True:
    GPIO.wait_for_edge(25, GPIO.RISING)
    # reading
    try:
        f = open(workfile, 'ab+')       # open for reading. If it does not exist, create it
        value = int(f.readline().rstrip())  # read the first line; it should be an integer value
    except:
        value = 0               # if something went wrong, reset to 0
    #print "old value is", value
    f.close()   # close for reading
    # writing
    f = open(workfile, 'w')
    f.write((str(value+1)+ '\n'))           # the value
    f.write((str(datetime.datetime.now())+ '\n'))   # timestamp
    f.close()

    GPIO.wait_for_edge(25, GPIO.FALLING)

GPIO.cleanup()
