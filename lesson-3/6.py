print('Задайте пожалуйста строку для подсчета частоты встречаемости конкретного символа')
s_inp = input()
print('Задайте символ, о котором вы хотите найти информацию - сколько раз он встречается в строке')
symb = input()
print(f'Столько раз встречается символ в строке - {sum(1 for i in s_inp if i == symb)}')