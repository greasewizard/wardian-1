#!/usr/bin/python3
import time 
import RPi.GPIO as io 

io.setwarnings(False)
io.setmode(io.BCM) 
power_pin = 26
io.setup(power_pin, io.OUT)

def on():
    #print("POWER ON")
    io.output(power_pin, True)
    getState()

def off():
    #print("POWER OFF")
    io.output(power_pin, False)
    getState()

def toggle():
    if (io.input(power_pin)):
        print("TOGGLE: Off")
    
    if (not io.input(power_pin)):
        print("TOGGLE: On")

    io.output(power_pin, not io.input(power_pin))

def getState():
    if (io.input(power_pin)):
        print("STATE: On")
        return True
    if (not io.input(power_pin)):
        print("STATE: Off")
        return False

#io.cleanup()
