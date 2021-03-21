from Les3_Module import prime_number, greatest_common_factor, least_common_multiple
from Les3_Module import input_word_check, input_number_check, input_word_check1, input_number_check1
from decimal import Decimal
from math import sqrt
import cmath
from collections import Counter
# Задание #1 - 3

while True:
    print("""Введите код режима работы программы:
    1 - Определить, является ли введенное число простым
    2 - нахождение наибольшего общего делителя
    3 - нахождение наименьшего общего кратного
    
    5 - выход
    """)

    code=str(input())
    
    # ОПРЕДЕЛЕНИЕ ПРОСТОТЫ ЧИСЛА
    
    if code == '1':
        prime_number(answ = code)
         
    # ОПРЕДЕЛЕНИЕ НАИБОЛЬШЕГО ОБЩЕГО ДЕЛИТЕЛЯ
    
    elif code == '2':
        greatest_common_factor(answ = code)

    # ОПРЕДЕЛЕНИЕ НАИМЕНЬШЕГО ОБЩЕГО КРАТНОГО

    elif code == '3':
        least_common_multiple(answ = code)

    elif code == '5':
        break

    elif str.isdigit(code) == False or ' ' in code:
        print('Неверный формат кода')
        
    else: 
        print('Неправильный код')

# Задание #4

word, key = input_word_check()

print('Слова и ключ введены правильно')

key_len = len(key)
encr_text = ""
for i in range(len(word)):
    encr_text += chr(ord(word[i]) ^ ord(key[i % key_len]))

print(repr(encr_text))

ans = input('Хотите расшифровать сообщение?:[y/n]')  
if (ans == 'y'):
    decr_text = ""
    for i in range(len(encr_text)):
        decr_text += chr(ord(encr_text[i]) ^ ord(key[i % key_len]))
    print(repr(decr_text))
elif (ans == 'n'):
    pass



# Задание #5


min1, max2 = input_number_check()

print('Задайте число, частоту встречаемоcти которого вы хотите найти в заданном диапозоне')
dig = str(input())
diap = int(max2) - int(min1) + 1
print('Частота встречаемости вашего числа', sum(int(min1) for i in range(int(min1), int(max2) + 1) if dig in str(i)))


# Задание #6


s = input_word_check1()
print(Counter(s))


# Задание #8


print('Для решения квадратного уравнения вида ax^2 + bx + c = 0 введите коэффициенты')


a, b, c = input_number_check1()
print (a, b, c)


# Для начала нам нужно определить дискриминант
a = Decimal(a)
b = Decimal(b)
c = Decimal(c)
D = Decimal(b ** 2 - 4 * (a * c))

print ('D =', D)
# После определения дискриминанта, сравниваем его с нулём, чтобы понять сколько корней имеет данное квадратное уравнение
if D == 0:
    print('Дискриминант равен нулю, есть только один корень')
    x = Decimal( -b / (2 * a))
    print (f'Корень найден: {x}\nРешение завершено.')
elif D > 0:
    print('Дискриминант больше нуля, есть два корня')
    x1 = (-b + Decimal(sqrt(D))) / (2 * a)
    x2 = (-b - Decimal(sqrt(D))) / (2 * a)
    print (f'Корни найдены: x1 = {x1} x2 = {x2}\nРешение завершено')
else:
    print('Дискриминант меньше нуля. Решение с использованием комплексных чисел')
    x1 = (float(-b) + cmath.sqrt(D)) / float(2 *a)
    x2 = (float(-b) - cmath.sqrt(D)) / float(2 *a)
    
    print (f'Корни найдены: x1 ={x1}, x2 ={x2}\nРешение завершено')