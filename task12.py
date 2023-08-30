import math

s = int(input("Введите сумму загаданных чисел: "))
p = int(input("Введите произведение загаданных чисел: "))
x1 = (s + math.sqrt(s**2 - 4 * p)) / 2
x2 = (s - math.sqrt(s**2 - 4 * p)) / 2
print(x1)
print(x2)
    