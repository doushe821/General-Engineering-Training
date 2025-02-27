import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)


pwm = GPIO.PWM(21, 1000)
pwm.start(0)

try:
    while 1:
        newS = int(input())
        pwm.ChangeDutyCycle(newS)
        print(3.3*newS/100)


finally:
    pwm.stop()
    GPIO.output(21, 0)
    GPIO.cleanup()