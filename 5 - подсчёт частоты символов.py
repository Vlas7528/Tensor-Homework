from collections import Counter
count = lambda text: Counter(text)
text = input('Введите текст: \n')
print(f'Частота символов в тексте:\n{count(text)}')