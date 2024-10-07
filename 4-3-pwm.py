import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin_out = 21
pin_led = 9
GPIO.setup(pin_out, GPIO.OUT)
GPIO.setup(pin_led, GPIO.OUT)
freq = 50
p = GPIO.PWM(pin_out, freq)
p_led = GPIO.PWM(pin_led, freq)
p.start(0)
p_led.start(0)
try:
    while True:
        duty_cycle = int(input())
        p.ChangeDutyCycle(duty_cycle)
        p_led.ChangeDutyCycle(duty_cycle)
        time.sleep(0.2)
        print("Предполагаемое напряжение на выходе RC цепи:", duty_cycle * 3.3 / 100)
finally:
    GPIO.output(pin_out, 0)
    GPIO.output(pin_led, 0)
    GPIO.cleanup()