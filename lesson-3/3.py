print('Введите 2 числа для нахождения наименьшего общего кратного')
while True:
    x = input('int: ')
    y = input('int: ') # int..
    try:
        x = int(x)
        y = int(y)
        break
    except:
        print('ошибка. Повторите ввод..')
print('Числа введено правильно')
z = 0
x = abs(x)
y = abs(y)
if x < y:
    x, y = y, x
r = x % y
while r != 0:
    x = y
    y = r
    r = x % y
z = abs(x * y) / y 
print('Наименьшее общее кратное равно =', z)