def write_to_file(data, filename):
    """Функция записи данных в файл.

    Записывает данные переменной data в файл по имени filename.
    Запись производится сразу в байтовом формате.
    """

    try:
        with open(filename, 'wb') as f:
            f.write(data)
    except Exception as error:
        print(f'Произошла ошибка: {error}.\nПопробуйте ещё раз!')
    

def read_from_file(filename):
    """Функция чтения данных из файла.

    Считывает данные из указанного по имени filename файла
    и возвращает их в байтовом формате.
    """
    try:
        with open(filename, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print('\n***Требуемый файл не обнаружен!!!***\n   Создайте необходимые файлы!')
        data = bytearray('Error', 'utf-8')
    return data