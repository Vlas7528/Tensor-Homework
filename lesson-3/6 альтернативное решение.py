# Для подсчёта количества букв в тексте используем функцию Counter

from collections import Counter
text = '[Введите текст]' 
print(' {:*^30} '.format(text))
s = str(input())
print(Counter(s))
