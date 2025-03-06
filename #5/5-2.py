import RPi.GPIO as GPIO
import time 

def dec2bin(n):
    return[int(element) for element in bin(n)[2:].zfill(8)]

def adc():
    k = 0
    for i in range (7, -1, -1):
        k += 2**i 
        dval = dec2bin(k)
        GPIO.output(dac, dval)
        time.sleep(0.01)       
        cval = GPIO.input(altComp)
        if cval:
            k -= 2**i
    return k
    

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