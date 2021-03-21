def random_key_gen(lenght):

    """Функция генерации случайного ключа длинной lenght.

    lenght - длина ключа (целое число)
    """

    import secrets
    import string
    # переменная содержащая набор английский строчных и заглавных букв и цифр.
    # образованна из набора функций string.ascii_letters и string.digits
    megastring = string.ascii_letters + string.digits
    # secrets.choice - возвращает случайный элемент из указанной последовательности
    # .join записывает результат выполнения в одну строку, используя при этом разделитель между элементами, указанный в ''.
    # Так как '' - пусты, значит всё будет записано слитно.
    key = ''.join(secrets.choice(megastring) for i in range(lenght))
    key = bytearray(key, 'utf-8')
    return key