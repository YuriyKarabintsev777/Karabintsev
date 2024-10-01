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
    answer = [0, 0, 0, 0, 0, 0, 0, 0]
    ind = 0
    while True:
        if ind == 7:
            break
        answer[ind] = 1
        GPIO.output(dac, answer)
        time.sleep(0.007)
        comp_out = GPIO.input(comp)
        if comp_out == 1:
            answer[ind] = 0
        ind += 1
    #result_number = answer[7] + answer[6] * 2 ** 1 + answer[5] * 2 ** 2 + answer[4] * 2 ** 3 + answer[3] * 2 ** 4 + answer[2] * 2 ** 5 + answer[1] * 2 ** 6 + answer[0] * 2 ** 7
    result_number = sum([answer[7 - i] * 2 ** i for i in range(8)])
    return result_number



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