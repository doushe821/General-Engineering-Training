import RPi.GPIO as GPIO
def dec2bin(n):
    return[int(element) for element in bin(n)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while 1:
        binary=[0]*8
        inp = input()
        try:
            inp = int(inp)
            GPIO.output(dac, dec2bin(inp))
            v = (float(inp) / 255.0) * 3.3 
            print(f"Current voltage: {v:.4}")
        except Exception:
            if inp == "q": break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()