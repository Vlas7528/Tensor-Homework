while True:
    list_one = [i for i in input('Введите значения списка через пробел:\n').split()]
    list_two = []
    try:
        for i in list_one:
            i = int(i)
        break
    except: 
        print('Неверный формат данных в списке')
print(f'Введенный список:       {list_one}')

# 1 способ - на выходе список с другой последовательностю измененного списка

# print(list_one)
# list_two = list(set(list_one))
# print(list_two)       


# 2 способ - с сохранением последовательности изначального списка 

for value in list_one:
    try:
        list_two.index(value)
    except:
        list_two.append(value)
list_one.clear()
for value in list_two:
    list_one.append(value)
list_two.clear()
print(f'Отсортированный список: {list_one}')

