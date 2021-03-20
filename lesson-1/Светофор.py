print('Введите код сигнала светофора, где:\n1 - Красный\n2 - Жёлтый\n3 - Зелёный')
color=int(input())
if color == 1:
    print('Стой')
elif color == 2:
    print('Ожидай смены сигнала')
elif color == 3:
    print('Иди')
else: 
    print('Неправильный код сигнала светофора')