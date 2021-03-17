
from os import error
import string
# Модуль secrets используется для генерации криптографически сильных случайных чисел
# Этот модуль следует использовать вместо генератора псевдослучайных чисел по умолчанию в модуле random, 
# который предназначен для моделирования и симуляции, а не безопасности или криптографии.
import secrets
# from typing import Text


def menu():
    while True:
        menu = input(
    """
    Выберите задачу.
    Зашифровать:...............1
    Расшифровать:..............2
    Сгенерировать ключ:........3
    Выход:.....................Enter
    """
        )
        if not menu:
            print("До свидания...")
            break
        elif menu == '1':
            xor_cipher()
        elif menu == '2':
            decryption()
        elif menu == '3':
            random_key()
        else:
            print("Повторите ввод...")



def write_to_file(data, filename):
    try:
        with open(filename, 'wb') as f:
            f.write(data)
    except Exception as error:
        print(f'Произошла ошибка: {error}.\nПопробуйте ещё раз!')
    

def read_from_file(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print('\n***Требуемый файл не обнаружен!!!***\n   Создайте необходимые файлы!')
        # Отсылаем пользователя обратно в меню программы, если нет нужного для чтения файла
        menu()
    return data

def random_key():
    while True:
        lenght = input('Укажите желаемую длину ключа в символах (целое число):\n')
        try:
            lenght= int(lenght)
            break
        except:
            print('Попробуйте ещё раз!')
    lenght=int(lenght)
    # переменная содержащая набор английский строчных и заглавных букв и цифр.
    # образованна из набора функций string.ascii_letters и string.digits
    megastring = string.ascii_letters + string.digits
    # secrets.choice - возвращает случайный элемент из указанной последовательности
    # .join записывает результат выполнения в одну строку, используя при этом разделитель между элементами, указанный в ''.
    # Так как '' - пусты, значит всё будет записано слитно.
    key = ''.join(secrets.choice(megastring) for i in range(lenght))
    key = bytearray(key, 'utf-8')
    print(f'Сгенерированный ключ: {key}')
    write_to_file(key, './key.txt')


def xor_cipher():
    text = input('Введите текст, который Вы хотите зашифровать (Enter - прочитать текст из файла text.txt')
    if not text:
        text = read_from_file('./text.txt')
    key = input('''
    Введите ключ, которым Вы хотите произвести шифрование.
    Внимание! Это перезапишет ключ в файле key.txt, если он есть.
    (Enter - прочитать ключ из файла key.txt)
    ''')
    if not key:
       key = (read_from_file('./key.txt'))
       print(f'Используемый ключ: {key}')

    cipher = bytearray()
    # key = bytearray(key, 'utf-8')
    # text = bytearray(text, 'utf-8')
    # Переменная для подсчёта индекса, по которому мы будем обращаться к байт-массиву ключа
    b = int(0)
    for i in text:
        cipher.append(i ^ key[b])
        # При выполнении цикла первый раз, мы обратимся по индексу 0 и возьмем из байт-массива ключа первое значение.
        # После этого мы увеличиваем переменную индекса чтобы обратиться к следующему символу
        b+=1
        # когда символы ключа заканчиваются, мы снова начинаем обращаться к первому символу массива
        if b == len(key):
            b=0
    print('Зашифрованный текст сохранён в файл cipher_text.txt!')
    write_to_file(cipher, './cipher_text.txt')

def decryption():
    text = input('Напишите текст для расшифрования (Enter - прочитать текст из файла cipher_text.txt')
    if not text:
       text = read_from_file('./cipher_text.txt')
    key = input('''
    Введите ключ, которым Вы хотите произвести расшифрование.
    Внимание! Это перезапишет ключ в файле key.txt, если он есть.
    (Enter - прочитать ключ из файла key.txt)
    ''')
    if not key:
       key = read_from_file('./key.txt') 
    cipher = bytearray()
    # key = bytearray(key, 'utf-8')
    # text = bytearray(text, 'utf-8')
    b = int(0)
    for i in text:
        cipher.append(i ^ key[b])
        b+=1
        if b == len(key):
            b=0
    print('Расшифрованный текст сохранён в файл decrypted_text.txt!')
    write_to_file(cipher, './decrypted_text.txt')



    
menu()

