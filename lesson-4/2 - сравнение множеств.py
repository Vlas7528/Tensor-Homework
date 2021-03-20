while True:
    a = [i for i in input('Введите значения списка №1 через пробел:\n').split()]
    try:
        for i in a:
            i = int(i)
        break
    except: 
        print('Неверный формат данных в списке')

while True:
    b = [i for i in input('Введите значения списка №2 через пробел:\n').split()]
    try:
        for i in b:
            i = int(i)
        break
    except: 
        print('Неверный формат данных в списке')

print(f"""
Введенный список №1:                      {a}
Введенный список №2:                      {b}
""")



c = list(set(a) & set(b))
print('Совпадающие множества введенных списков:', c)