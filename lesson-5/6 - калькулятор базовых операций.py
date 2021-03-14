from decimal import Decimal
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