#!/usr/bin/python

import sys
import Adafruit_DHT
import csv
from datetime import datetime
import os.path

# constants
# sensor type and data pin
pin = 22
sensor = Adafruit_DHT.AM2302

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
# attempting to read from pin 22
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

def getReading():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return humidity, temperature
    else:
        return "Could not get reading from AM2302 sensor"


