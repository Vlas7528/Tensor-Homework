from functools import reduce
def factorial():
    n = get_int("Введите число: ")
    fact = 1
    if n > 0:
        # Функция reduce() это высокоуровневая импортируемая функция из модуля functools.
        # Принцип её работы описан ниже на примере кода.
        # Функиця reduce() берёт два аргумента из итерируемого объекта и передает эти знчаения в функцию lambda, 
        # которая получает два эти аргумента и перемножает их. После того, как lambda возвращает результат, reduce() принимает его
        # в качестве первого аргуемента, а в качестве второго принимает следующий элемент итерируемого объекта (3ье значение). После снова
        # отправляет два аргумента в функцию lambda до тех пор, пока не закончатся элементы итеруремого объекта. 
        
        # В качестве итерируемого объекта выступает список(list) - [y for y in range(1, n + 1)]
        # Список остается безымянным. Такая запись списка позволяет сделать последовательность натуральных чисело от 0 до введенного
        # в функции get_int() числа.
        fact = reduce((lambda x, y: x * y), [y for y in range(1, n + 1)])  # range(1, n + 1) образует диапазон от 1 (включительно) до n + 1 (не включительно)
        # Выводится переменная n (введенное в get_int() число) и результат выполнения функции reduce() выше.
        print(f"{n}! = {fact}")
    else:
        print(
            "Факториал может быть определен только для натуральных чисел. Попробуйте снова."
        )

# Функция проверки введенного числа
def get_int(message):
    # переменной number присваиватеся ноль
    number = 0
    # пока number равна нулую:
    while not number:
        # происходит запись в переменную string ввода пользователя. (в качестве подсказки/приглашению к вводу исползуется текст
        # переменной message)
        string = input(message)
        # Конструкция try.. except. Если блок try завершится с ошибкой, будет выполнен код в блоке except.
        try:
            # Используем конструкт int на переменной string. Так мы проверим, является ли число натуральным.
            number = int(string)
        except Exception as exc:
            # Если число не натуральное - получим сообщение и цикл продолжится пока мы не введём допустимое число.
            print("Что-то пошло не так, попробуйте снова...")
            # Цикл так же не будет завершён, пока не изменится значение переменной number
    return number

factorial()