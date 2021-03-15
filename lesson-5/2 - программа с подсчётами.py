def dz2_1(s, **word_count_dictionary):

        word_count_dictionary = {}

        for c in s:
            if c not in word_count_dictionary:
                word_count_dictionary[c] = 1
            else:
                word_count_dictionary[c] += 1

        print('Частота встречаемости каждого символа в введенной вами строке:  ', word_count_dictionary)



def dz2_2(s, word_count,symb_count):
    symbol_open = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
      'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3' ,'4', '5', '6', '7', '8', '9')
    symbol_close = (')', ']', '}', '>', ' ', ',' , '!' , '?', ':', ';', '.')
    is_prev_char_letter = False
    for i in range(len(s)):
        if i == len(s) - 1 and s[i] in symbol_open:
            word_count += 1
        elif s[i] in symbol_close and is_prev_char_letter == True:                                
            word_count += 1
        is_prev_char_letter = s[i] in symbol_open
    print('Количество слов:   ', word_count) 


def dz2_3(s, sentence_count, symb_count):
    symbol_open = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
      'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3' ,'4', '5', '6', '7', '8', '9')
    is_prev_char_letter = False
    for i in range(len(s)):
        if s[i] == '.' or s[i] == '!' or s[i] == '?' and is_prev_char_letter == True:
            sentence_count += 1
        elif i == len(s) - 1 and s[i] in symbol_open:
            sentence_count += 1
    is_prev_char_letter = s[i] in symbol_open
    print('Количество предложений:   ', sentence_count) 

# print(dz2_3(s = s1, sentence_count = senc,  symb_count = sc))


while True:
    s1 = input('Введите слово, набор слов или набор предложений  ')
    answ = input('''Чего вы хотите?
        1. Посчитать частоту вхождения символов в строке
        2. Посчитать количество слов в введенном вами тексте
        3. Посчитать количество предложений в введенном вами тексте)  
    ''')
    try:
        # word = str(word)
        # key = str(key)
        # break
        answ = int(answ)
        pass
    except:
        print('ошибка. Повторите ввод..')
        break
    if (s1.isdigit()):
        continue
    # if (answ.isalpha()):
    #     continue
    else:
        break
print('Слова введены правильно')
wcd = 0
wc = 0
sc = 0
senc = 0

if answ == 1:
    print(dz2_1(s = s1, word_count_dictionary = wcd))
elif answ == 2:  
    print(dz2_2(s = s1, word_count = wc, symb_count = sc ))
if answ == 3:
    print(dz2_3(s = s1, sentence_count = senc,  symb_count = sc))
