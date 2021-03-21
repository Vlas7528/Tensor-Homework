from random import randint

def input_check():
    while True:
        n = input('Введите длину массива: ')
        try:
            n = int(n)
            break
        except:
            print('\nНеверный формат числа!')
    # countx подсчитывает какое число мы вводим в данный момент
    countx = 1
    # Объявляем список (массив) 
    mas = []
    menu =input(
    """ 
    Написать числа самому:                1
    Сгенерировать числа автоматически:    2  
    """)  
    # Цикл не закончится, пока не введем все числа
    if menu == '1':
        for i in range(n):
            while True:
                x = input(f'Введите число {countx}: ')
                try:
                    x = int(x)
                    break
                except:
                    print('\nНеверный формат числа!')
                    i = i-1
            mas.append(x)
            countx+=1
    elif menu == '2':
        for i in range(n):
            mas.append(randint(1,99))
    else:
        print('\nНеверный код!')
        input_check()

    return n, mas


def input_check1():
    while True:
        a = [i for i in input('Введите значения списка №1 через пробел:\n').split()]
        try:
            for i in a:
                i = int(i)
            break
        except: 
            print('Неверный формат данных в списке')

    while True:
        b = [i for i in input('Введите значения списка №2 через пробел:\n').split()]
        try:
            for i in b:
                i = int(i)
            break
        except: 
            print('Неверный формат данных в списке')
    return a, b


def input_check2():
    while True:
        list_one = [i for i in input('Введите значения списка через пробел:\n').split()]
        try:
            for i in list_one:
                i = int(i)
            break
        except: 
            print('Неверный формат данных в списке')
    return list_one
    

def input_check3():
    while True:
        str_inp = input('Введите строку с случайным расположением скобок в ней:   ')
        try:
            pass
        except:
            break
        if (str_inp.isdigit()):
            pass
            print('ошибка. Повторите ввод..')
        else:
            break
    return str_inp

