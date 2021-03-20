while True:
    print("""
    Для начала введите - 1
    Для выхода введите - 5
    """)
    menu=int(input())
    if menu == 5:
        break
        
    elif menu == 1:
        pass
    else: 
        print('Неправильный код!')
        break
    text = '[Введите диапазон чисел]' 
    print(' {:*^30} '.format(text))
    print('Подсказка. Диапазон включает первое число и продолжается до второго числа, не включая его.')
    n1 = (input('Введите первое число -> '))
    n2 = (input('Введите второе число -> '))


    if str.isdigit(n1) == True and str.isdigit(n2) == True:
        if int(n1) >= int(n2):
            print('Первое число не может быть больше или равно второму')
            break
        n1 = int(n1)
        n2 = int(n2)
    

        x0 = int(0)
        x1 = int(0)
        x2 = int(0)
        x3 = int(0)
        x4 = int(0)
        x5 = int(0)
        x6 = int(0)
        x7 = int(0)
        x8 = int(0)
        x9 = int(0)

        lists = list(range(n1, n2))
        result = str("".join([str(l) for l in lists]))
        print(result)

        for i in result:
            if i == '0':
                x0 = x0 + 1

            elif i == '1':
                x1 = x1 + 1

            elif i == '2':
                x2 = x2 + 1

            elif i == '3':
                x3 = x3 + 1

            elif i == '4':
                x4 = x4 + 1

            elif i == '5':
                x5 = x5 + 1

            elif i == '6':
                x6 = x6 + 1

            elif i == '7':
                x7 = x7 + 1

            elif i == '8':
                x8 = x8 + 1

            elif i == '9':
                x9 = x9 + 1

        print(f"""
        Частота цифр в диапазоне:
        Цифра 0 - {x0}
        Цифра 1 - {x1}
        Цифра 2 - {x2}
        Цифра 3 - {x3}
        Цифра 4 - {x4}
        Цифра 5 - {x5}
        Цифра 6 - {x6}
        Цифра 7 - {x7}
        Цифра 8 - {x8}
        Цифра 9 - {x9}
        """)


    else:
        print('Неверный формат чисел')
    
