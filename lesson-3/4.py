while True:
    word = input('Введите слово для зашифрования:  ')
    key = input('Введите ключ для реализации шифрования(ключ должен иметь такое же количество букв, что и введенное слово:   ') # int..
    try:
        pass
    except:
        print('ошибка. Повторите ввод..')
        break
    if (word.isdigit()):
        continue
    if (key.isdigit()):
        continue
    else:
        break
print('Слова и ключ введены правильно')

key_len = len(key)
encr_text = ""
for i in range(len(word)):
    encr_text += chr(ord(word[i]) ^ ord(key[i % key_len]))

print(repr(encr_text))

ans = input('Хотите расшифровать сообщение?:[y/n]')  
if (ans == 'y'):
    decr_text = ""
    for i in range(len(encr_text)):
        decr_text += chr(ord(encr_text[i]) ^ ord(key[i % key_len]))
    print(repr(decr_text))
elif (ans == 'n'):
    pass