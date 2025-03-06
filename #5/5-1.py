import RPi.GPIO as GPIO
import time 

def dec2bin(n):
    return[int(element) for element in bin(n)[2:].zfill(8)]

def adc():
    for i in range (256):
            GPIO.output(dac, dec2bin(i))
            if GPIO.input(comp) == 1:
                time.sleep(0.1)
                return i/2
    time.sleep(0.1)
    return 0
    

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14 
troyka = 13 
altComp = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(altComp, GPIO.OUT)
GPIO.output(altComp, GPIO.input(comp))

try: 
    while True:
        n = adc()
        if n:
            print("Voltage is {:.2f}".format(n*3.3/256))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("Program ended")
