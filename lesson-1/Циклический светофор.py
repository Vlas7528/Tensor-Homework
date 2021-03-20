while True:
    print('Введите код сигнала светофора, где:\n\n 1 - Красный\n 2 - Жёлтый\n 3 - Зелёный\n\nДля выхода из программы введите 5')
    color=int(input())
    if color == 1:
        print('Стой')
    elif color == 2:
        print('Ожидай смены сигнала')
    elif color == 3:
        print('Иди')
    elif color == 5:
        break
    else: 
        print('Неправильный код сигнала светофора')