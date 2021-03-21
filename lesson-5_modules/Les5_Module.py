from decimal import Decimal


def input_check():
    while True:
        x = input('Введите число для подсчета факториала: ') # int..
        try:
            x = int(x)
            break
        except:
            print('ошибка.Введено не число. Повторите ввод..')
    return x


def input_check1():
    while True:
        s1 = input('Введите слово, набор слов или набор предложений  ')
        answ = input('''Чего вы хотите?
            1. Посчитать частоту вхождения символов в строке
            2. Посчитать количество слов в введенном вами тексте
            3. Посчитать количество предложений в введенном вами тексте)  
        ''')
        try:
            answ = int(answ)
            pass
        except:
            break
        if (s1.isdigit()):
            print('ошибка. Повторите ввод..')
            continue
        else:
            break
    return s1, answ


def input_check2():
    while True:
        sum = input ('Введите сумму вклада в рублях -> ')
        percent = input ('Введите значение начисляющихся процентов каждый месяц -> ')
        months = input ('Введите количество месяцев (цело число) -> ')
        print('*** Проверка введенных чисел... ***')
        try: 
            sum = Decimal(sum)
            percent = Decimal(percent)
            months = int(months)
            break
        except Exception as e:
            print('Неверный формат введенных чисел. Повторите ввод.')
    return sum, percent, months


def input_check3_1():
    while True:
        x1 = input ('Введите первое число:\n')
        x2 = input ('Введите второе число:\n')
        try:
            x1 = Decimal(x1)
            x2 = Decimal(x2)
            break
        except Exception as e:
            print('Неверный формат данных')
    return x1, x2


def input_check3_2():
    while True:
        x3 = input ('Введите следущее число (Enter чтобы завершить вычисления):\n')
        if not x3:
            print('До свидания...')
            menu = False
            break
        try:
            x3 = Decimal(x3)
            break
        except:
            print('Неверный формат данных')
    return x3, menu