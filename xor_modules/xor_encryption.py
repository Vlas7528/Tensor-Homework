def xor_func(text, key):

    """Функция xor обработки входящих переменных. (Логическое ИЛИ)

    text - переменная, к каждому символу которой будет применено логическое 
    "ИЛИ" на символы перменной key.
    key - переменная, символы от которой берутся циклически
    file_in - str название файла, в который будет записываться результат
    file_out - str название файла, из которого будет прочитываться текст
    """

    cipher = bytearray()    
    # b - переменная для подсчёта индекса, по которому мы будем обращаться 
    # к байт-массиву ключа
    b = int(0)
    for i in text:
        cipher.append(i ^ key[b])
        # При выполнении цикла первый раз, мы обратимся по индексу 0 и возьмем 
        # из байт-массива ключа первое значение.
        # После этого мы увеличиваем переменную индекса чтобы обратиться к 
        # следующему символу.
        b+=1
        # Когда символы ключа заканчиваются, мы снова начинаем обращаться 
        # к первому символу массива.
        if b == len(key):
            b=0
    return(cipher)