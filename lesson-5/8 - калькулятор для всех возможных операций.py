# Импортируем необходимы для работы модули
from decimal import Decimal
from math import sqrt
# Пустой список, в который каждый раз будет дописываться результат вычислений
result = []
# Ниже описаны функции для каждого из всех математических дейтсвий, доступных в калькуляторе
# Сложение
def plus(n1, n2):
    n3 = n1 + n2
    # в каждой математической функции в конце в список result добавляется полученный результат 
    result.append(n3)
    return n3
# Вычитание
def minus(n1, n2):
    n3 = n1 - n2
    result.append(n3)
    return n3
# Деление
def division(n1, n2):
    # Проверка деления на ноль
    try: 
        n3 = n1 / n2
    except:
        print('На ноль делить нельзя!')
        # Если проверка провалена - калькулятор запускается заново.
        calc()
    n3 = n1 / n2
    result.append(n3)
    return n3
# Умножение
def multiplication(n1, n2):
    n3 = n1 * n2
    result.append(n3)
    return n3
# Возведение в степень
def exponentiation(n1, n2):
    n3 = n1 ** n2
    result.append(n3)
    return n3
def sqrtfunc(n1):
    n3 = sqrt(n1)
    result.append(n3)
    return n3
def division2(n1, n2):
    n3 = n1 // n2
    result.append(n3)
    return n3
def division3(n1, n2):
    n3 = n1 % n2
    result.append(n3)
    return n3
# Сама программа калькулятор:
def calc():
    # Проверка введенных чисел
    while True:
        x1 = input ('Введите первое число:\n')
        x2 = input ('Введите второе число:\n')
        try:
            x1 = Decimal(x1)
            x2 = Decimal(x2)
            break
        except Exception as e:
            # print(e) - раскомментировать чтобы выводить тип ошибки
            print('Неверный формат данных')
    # Проверка введенного символа операции
    while True:
        opr = input ("""
        Введите требуемую операцию:
        + сложение
        - вычитание
        / деление
        * умножение
        ** возведение в степень
        sqrt вычислить квадратный корень из первого числа (или имеющегося результата)
        // получение целой части от деления
        % получение остатка от деления

        """)
        # В зависимости от символа, программа обращается к нужной функции, передавая в качестве аргумента значения 
        # двух, введенных ранее, чисел
        if opr == '+':
            print(f'Результат: {plus(x1, x2)}')
            break
        elif opr == '-':
            print(f'Результат: {minus(x1, x2)}')
            break
        elif opr == '/':
            print(f'Результат: {division(x1, x2)}')
            break
        elif opr == '*':
            print(f'Результат: {multiplication(x1, x2)}')
            break
        elif opr == '**':
            print(f'Результат: {exponentiation(x1, x2)}')
            break
        elif opr == 'sqrt':
            print(f'Результат: {sqrtfunc(x1)}')
            break
        elif opr == '//':
            print(f'Результат: {division2(x1, x2)}')
            break
        elif opr == '%':
            print(f'Результат: {division3(x1, x2)}')
            break
        else:
            print('Неверный код операции!')
    # Показывает сколько шагов вычислений уже было совершено. Переменная нужна для обращению по индексу к списку
    count = int(0)
    # Пока у этой переменной значение True, следующий цикл будет выполняться
    menu = True
    while menu == True:
        # Теперь мы вводим не два числа, как раньше - а только одно.
        while True:
            x3 = input ('Введите следущее число (Enter чтобы завершить вычисления):\n')
            # Если нажать Enter ничего не вводя - программа завершится
            if not x3:
                print('До свидания...')
                menu = False
                # Выходим из цикла while True:
                break
            # Проверка введенного числа
            try:
                x3 = Decimal(x3)
                break
            except:
                print('Неверный формат данных')
        # Если мы нажали Enter - программа завершается, не начиная следующий цикл.
        if menu == False:
            # Выходим из цикла while menu == True:
            break
        # Снова цикл расчётов. Отличие только в том, что в качестве первого аргумента мы передаем 
        # последнее значение из списка result, а в качетсве второго - число которое ввели.
        while True:
            opr = input ("""
        Введите требуемую операцию:
        + сложение
        - вычитание
        / деление
        * умножение
        ** возведение в степень
        sqrt вычислить квадратный корень из первого числа (или имеющегося результата)
        // получение целой части от деления
        % получение остатка от деления

        """)
            if opr == '+':
                print(f'Результат: {plus(result[count], x3)}')
                break
            elif opr == '-':
                print(f'Результат: {minus(result[count], x3)}')
                break
            elif opr == '/':
                print(f'Результат: {division(result[count], x3)}')
                break
            elif opr == '*':
                print(f'Результат: {multiplication(result[count], x3)}')
                break
            elif opr == '**':
                print(f'Результат: {exponentiation(result[count], x3)}')
                break
            elif opr == 'sqrt':
                print(f'Результат: {sqrtfunc(result[count])}')
                break
            elif opr == '//':
                print(f'Результат: {division2(x1, x2)}')
                break
            elif opr == '%':
                print(f'Результат: {division3(x1, x2)}')
                break
            else:
                print('Неверный код операции!')
        # В конце каждого выполненного действия, увеличивается счётчик количества операций (нужен для обращения по индексу)
        count += 1
    # В случае закрытия программы, выводятся результаты всех вычислений
    print(f'Расчёты завершены.\nИстория вычислений:{result}\nКол-во операций: {count+1}')
calc()