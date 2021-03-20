print('Введите любое число, чтобы проверить является ли оно простым')
number_list = []
           
while True:
    x = input('int: ') # int..
    try:
        x = int(x)
        break
    except:
        print('ошибка. Повторите ввод..')
print('Число введено правильно')            
if (x == 1):
    print('Ваше число простое')
for i in range(1, x + 1):
    if (x % i == 0):
        number_list.append(i)
if len(number_list) == 2:
    print('Ваше число простое')
elif len(number_list) != 2:
    print('Число не простое')