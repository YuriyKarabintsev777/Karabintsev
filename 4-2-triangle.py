import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
period = 10

def decimal2binary(number):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    ind = 7
    while number:
        result[ind] = number % 2
        number = number // 2
        ind -= 1
    return result

try:
    while 1:
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(period / 512)
        for i in range(255, 1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(period / 512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()