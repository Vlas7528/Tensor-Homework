while True:
    x = input('int: ') # int..
    try:
        x = int(x)
        break
    except:
        print('ошибка.Введено не число. Повторите ввод..')
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
        for i in range(1 , a):
            if i > 2:
                multi = b
                b = multi * (i + 1)
            else:
                multi = i
                b = multi * (i + 1)
               
        print('Факториал числа равен:  ', b)
                


print(dz1(a = x , multi = y, b = z))
