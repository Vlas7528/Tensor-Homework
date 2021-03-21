from Les5_Module import input_check, input_check1, input_check2, input_check3_1, input_check3_2
from decimal import Decimal
from math import sqrt
import math
from functools import reduce
# Задание #1

x = input_check()

print('Число введено правильно')

y = 1
z = 0

def dz1(a, b, multi):
    if a == 0:
        a = 1
        print('Факториал числа равен:  ', a)
    elif a == 1:
        print('Факториал числа равен:  ', a)
    elif a > 1:
        for i in range(1, a):
            if i > 2:
                multi = b
                b = multi * (i + 1)
            else:
                multi = i
                b = multi * (i + 1)
               
        print('Факториал числа равен:  ', b)
                
print(dz1(a = x , multi = y, b = z))


# Задание #2


def dz2_1(s, **word_count_dictionary):

        word_count_dictionary = {}

        for c in s:
            if c not in word_count_dictionary:
                word_count_dictionary[c] = 1
            else:
                word_count_dictionary[c] += 1

        print('Частота встречаемости каждого символа в введенной вами строке:  ', word_count_dictionary)


def dz2_2(s, word_count,symb_count):
    symbol_open = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3' ,'4', '5', '6', '7', '8', '9'
                  )
    symbol_close = (')', ']', '}', '>', ' ', ',',
                    '!', '?', ':', ';', '.'
                   )
    is_prev_char_letter = False
    for i in range(len(s)):
        if i == len(s) - 1 and s[i] in symbol_open:
            word_count += 1
        elif s[i] in symbol_close and is_prev_char_letter == True:                                
            word_count += 1
        is_prev_char_letter = s[i] in symbol_open
    print('Количество слов:   ', word_count) 


def dz2_3(s, sentence_count, symb_count):
    symbol_open = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3' ,'4', '5', '6', '7', '8', '9'
                  )
    is_prev_char_letter = False
    for i in range(len(s)):
        if s[i] == '.' or s[i] == '!' or s[i] == '?' and is_prev_char_letter == True:
            sentence_count += 1
        elif i == len(s) - 1 and s[i] in symbol_open:
            sentence_count += 1
    is_prev_char_letter = s[i] in symbol_open
    print('Количество предложений:   ', sentence_count) 

# print(dz2_3(s = s1, sentence_count = senc,  symb_count = sc))

s1, answ = input_check1()

print('Слова введены правильно')
wcd = 0
wc = 0
sc = 0
senc = 0

if answ == 1:
    print(dz2_1(s = s1, word_count_dictionary = wcd))
elif answ == 2:  
    print(dz2_2(s = s1, word_count = wc, symb_count = sc ))
if answ == 3:
    print(dz2_3(s = s1, sentence_count = senc,  symb_count = sc))


# Задание #3


def bank(sum, percent, months):
    for i in range(months):
        print (f'Сумма вклада за месяц {i+1} выросла на {round(((sum*percent)/100), 3)}')
        sum = sum + ((sum * percent) / 100)
        print (f'и составила {round(sum, 3)} рублей\n')
    return sum

sum, percent, months = input_check2()
        
print(f'Рассчитанная сумма вклада: {round(bank(sum, percent, months), 3)} рублей')


# Задание #4


f = lambda x: math.factorial(x)
x = input_check()
print(f'Факториал числа {x} равен {f(x)}')


# Задание #5


result = []
def plus(n1, n2):
    n3 = n1 + n2
    result.append(n3)
    return n3
def minus(n1, n2):
    n3 = n1 - n2
    result.append(n3)
    return n3
def division(n1, n2):
    try: 
        n3 = n1 / n2
    except Exception as e:
        # print(e)
        print('На ноль делить нельзя!')
        calc()
    n3 = n1 / n2
    result.append(n3)
    return n3
def multiplication(n1, n2):
    n3 = n1 * n2
    result.append(n3)
    return n3
def exponentiation(n1, n2):
    n3 = n1 ** n2
    result.append(n3)
    return n3

def calc():
    x1, x2 = input_check3_1()
    while True:
        opr = input ('Введите требуемую операцию:\n')
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
        else:
            print('Неверный код операции!')
    count = int(0)
    menu = True
    while menu == True:
        x3 = input_check3_2(menue = menu)
        if menu == False:
            break
        while True:
            opr = input('Введите требуемую операцию:\n')
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
            else:
                print('Неверный код операции!')
        count += 1
    print(f'Расчёты завершены. История вычислений:{result}')
calc()


# Задание #7


n = input_check()
print (reduce(lambda x, y : x * y, range(1, n + 1)))


# Задание #8


# Импортируем необходимы для работы модули

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
    x1, x2 = input_check3_1()
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
        x3, menu = input_check3_2()
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
                        q - выйти
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