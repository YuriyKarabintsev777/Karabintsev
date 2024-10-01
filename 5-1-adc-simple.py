import RPi.GPIO as GPIO
import time

def decimal2binary(number):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    ind = 7
    while number:
        result[ind] = number % 2
        number = number // 2
        ind -= 1
    return result

def adc():
    for value in range(0, 256):
        GPIO.output(dac, value)
        out_signal = decimal2binary(value)
        GPIO.output(dac, out_signal)
        time.sleep(0.007)
        got = GPIO.input(comp)
        if got == 1:
            return value
    return 0


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        n = adc() 
        print("Number:", n, "Voltage:", n * 3.3 / 256)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()