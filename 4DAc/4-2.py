import RPi.GPIO as GPIO
import time
#import pyplot as plt 
#import numpy as np

def dec2bin(n):
    return[int(element) for element in bin(n)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

x = 0
flag = 1

try:
    T = float(input("Period:"))
    while 1:
        GPIO.output(dac, dec2bin(x))

        if x == 0: flag = 1
        elif x == 255: flag = 0
        if flag == 1:
            x = x + 1
        else: 
            x = x - 1    
        time.sleep(T/512)


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()