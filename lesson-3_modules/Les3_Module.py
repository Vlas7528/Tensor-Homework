from decimal import Decimal
import decimal


def prime_number(answ):
    if answ == '1':
        print('Является ли введенное число простым? Введите целое положительное число')
        n = input()
        i = int(2)
        j = int(0)

        # Функция проверки строки str.isdigit позволит ввести пользователю только целое положительное число. 
        if str.isdigit(n):
        # Перевод строки n в формат данных целого числа для дальнейших расчётов
            n = int(n)
        # Для определения простоты числа использую алгоритм "Перебор делителей"
            while i * i <= n and j != 1 :
                if n % i == 0:
                    j = 1
                    i = i + 1
                else:
                    i = i + 1
            if j == 1:
                print(f'{n} это составное число')
            else:
                print(f'{n} это простое число')
        else:
            print('Неправильный формат числа')


def greatest_common_factor(answ):
    number = True
    while number == True:
        if answ == '2':
            print('нахождение наибольшего общего делителя  (НОД)')
            
            x1 = input('Введите первое число -> ')
            x2 = input('Введите второе число -> ')
            # Проверяем, ввел ли пользователь целое положительное число
            if str.isdigit(x1) == False or str.isdigit(x2) == False:
                print('Неправильный формат числа')
                break
            # Проверка завершена, переходим к расчётам c помощью Алгоритма Евклида
            x1 = int(x1)
            x2 = int(x2)
            while x1 != 0 and x2 != 0:
                if x1 > x2:
                    x1 = x1 % x2
                else:
                    x2 = x2 % x1

            print(f'НОД = {x1+x2}')
            number = False


def least_common_multiple(answ):
    number = True
    while number == True:
        if answ == '3':
            print('нахождение наименьшего общего кратного (НОК)')
            
            # Исходя из формулы НОК(a, b)=a·b:НОД(a, b). мы можем вычислить НОК используя предыдущий Алгоритм Евклида
            x1 = input('Введите первое число -> ')
            x2 = input('Введите второе число -> ')
            # Проверяем, ввел ли пользователь целое положительное число
            if str.isdigit(x1) == False or str.isdigit(x2) == False:
                print('Неправильный формат числа')
                break
            # Проверка завершена, переходим к расчётам c помощью Алгоритма Евклида
            x1 = int(x1)
            #  Сохраняем введенные значения переменных в отдельную переменную, так как в будущем они нам понадобятся
            x1_1 = x1
            x2 = int(x2)
            x2_1 = x2
            while x1 != 0 and x2 != 0:
                if x1 > x2:
                    x1 = x1 % x2
                else:
                    x2 = x2 % x1
            
            print(f'НОК = {(x1_1*x2_1)/(x1+x2)}')
            number = False


def input_word_check():
    while True:
        word1 = input('Введите слово для зашифрования:  ')
        key1 = input('Введите ключ для реализации шифрования(ключ должен иметь такое же количество букв, что и введенное слово):  ') # int..
        try:
            pass
        except:
            break
        if (word1.isdigit()):
            print('ошибка. Повторите ввод..')
            continue
        if (key1.isdigit()):
            print('ошибка. Повторите ввод..')
            continue
        else:
            break
    return word1, key1


def input_number_check():
    while True: 
        minimum = input('Задайте начало диапазона:  ') 
        maximum = input('Задайте конец диапозона:  ')
        try:
            minimum = int(minimum)
            maximum = int(maximum)
            break
        except:
            print('ошибка. Повторите ввод..')

    print('Числа диапозона введены правильно')
    return minimum, maximum
    

def input_word_check1():
    while True:
        text = input('Введите текст:  ') # int..
        try:
            pass
        except:
            break
        if (text.isdigit()):
            print('ошибка. Повторите ввод..')
            continue
        else:
            break
    return text


def input_number_check1():
    while True:
        a = input('Введите коэффициент a -> ')
        try:
            a = Decimal(a)
            break
        except:
            print('Неверный формат числа')
    while True:
        b = input('Введите коэффициент b -> ')
        try:
            b = Decimal(b)
            break
        except:
            print('Неверный формат числа')
    while True:        
        c = input('Введите коэффициент c -> ')
        try:
            c = Decimal(c)
            break
        except:
            print('Неверный формат числа')
    return a, b, c