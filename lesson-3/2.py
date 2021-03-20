print('Введите 2 числа для нахождения наибольшего общего делителя')

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
x = abs(x)
y = abs(y)
if x < y:
    x, y = y, x
r = x % y
while r != 0:
    x = y
    y = r
    r = x % y
print('Наибольший общий делитель равен', y)
