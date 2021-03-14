import math
f = lambda x: math.factorial(x)
while True:
    x = input('Введите число:\n')
    try:
        x = int(x)
        break
    except:
        print('Неверный формат числа')
print(f'Факториал числа {x} равен {f(x)}')