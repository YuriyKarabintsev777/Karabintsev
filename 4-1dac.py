import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(number):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    ind = 7
    while number:
        result[ind] = number % 2
        number = number // 2
        ind -= 1
    return result

try:
    while True:
        n = input()
        if n == "q":
            break
        if "." in n:
            work = n.split(".")
            if len(work) > 2:
                print("Не числовое значение.")
                continue
            for i in work:
                if i.isdigit() == False:
                    print("Не числовое значение.")
                    continue
            print("Ввод не целого значения.")
            continue
        if float(n) < 0:
            print("Отрицательное значение.")
            continue
        if (n.isdigit() == False):
            print("Не числовое значение.")
            continue
        n = int(n)
        if n > 255:
            print("Значение превышает возможности 8-разрядного ЦАП.")
            continue
        GPIO.output(dac, decimal2binary(n))
        print("Предполагаемое напряжение на ЦАП:", n * (3.3 / 2 ** 8), "B")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
