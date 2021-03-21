import xor_modules as xor

def menu():
    while True:
        menu = input(
    """
    Выберите задачу.
    xor шифрование:............1
    Сгенерировать ключ:........2
    Выход:.....................Enter
    """
        )
        if not menu:
            print("До свидания...")
            break
        elif menu == '1':
            xor_cipher()
        elif menu == '2':
            keygen()
        else:
            print("Повторите ввод...")

def keygen():
    
    while True:
        lenght = input('Укажите желаемую длину ключа в символах (целое число):\n')
        try:
            lenght= int(lenght)
            break
        except:
            print('Попробуйте ещё раз!')
    key = (xor.random_key_gen(lenght))
    print(f'Сгенерированный ключ: {key}')
    xor.write_to_file(key, './key.txt')

def xor_cipher():
    text = input('''
Введите текст, к которому Вы хотите применить xor 
шифрование (Enter - прочитать текст из файла)
    ''')
    text = bytearray(text, 'utf-8')
    if not text:
        file_name = input('Введите имя файла в формате name.txt\n')
        full_file_name = './' + file_name
        print(full_file_name)
        text = xor.read_from_file(full_file_name)
    key = input('''
Введите ключ, которым Вы хотите произвести шифрование.
(Enter - прочитать ключ из файла key.txt)
    ''')
    key = bytearray(key, 'utf-8')
    if not key:
       key = (xor.read_from_file('./key.txt'))
       print(f'Используемый ключ: {key}')
    cipher = (xor.xor_func(text, key))
    file_name = input('''
Введите имя файла в формате name.txt куда Вы хотите сохранить
обработанный текст. (Enter - сохранить в cipher_text.txt)
    ''')
    if not file_name:
        file_name = ('cipher_text.txt')
        print('Обработанный текст сохранен в файл cipher_text.txt')
    full_file_name = './' + file_name
    xor.write_to_file(cipher, full_file_name)

if __name__ == '__main__':
    menu()

