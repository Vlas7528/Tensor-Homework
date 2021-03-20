while True:
    str_inp = input('Введите строку с случайным расположением скобок в ней:   ')
    try:
        pass
    except:
        break
    if (str_inp.isdigit()):
        pass
        print('ошибка. Повторите ввод..')
    else:
        break
print('Строка введена верно')

def check(string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = []
    for i in string:
        if i in brackets_open: #если в данном индексе есть какая-либо из открывающегося типа скобок, то
            stack.append(i) #то добавляем её в стэк
        if i in brackets_closed:#если вдруг открывающейся скобки такого же типа не было, а мы нашли только закрывающююся скобку то ...    
            if len(stack) == 0:#то в стэк мы ничего не добавляли значит его длина равна 0 и скобки расставлены неверно
                return False
            index = brackets_closed.index(i) #сюда мы перешли, если открывающаяся скобка и закрывающаяся совпадают - кладем в значение index, индекс закрывающейся скобки
            open_bracket = brackets_open[index]#в переменную open_bracket кладем открывающейся скобку по раннее полученному индексу
            if stack[-1] == open_bracket:#идем в обратную сторону по стэку для удаления всех скобок если они расставлены правильно(нужно, чтобы очистить стэк), если он пустой то цикл завершается
                stack = stack[:-1]  
            else: return False  
    return (not stack)

if check(str_inp) == True:
    print('Скобки в введенной вами строке написаны верно')
else:
    print('Скобки в вашей строке расставлены неверно')