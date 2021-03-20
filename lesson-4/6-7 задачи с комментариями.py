class Tree:
    def __init__(self):
        self.root = None  # создание экземпляра класса Point и создание в нём переменной root 

	# возврат корневого узла
    def get_root(self):
        return self.root

	# добавление узла
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add(value, self.root)
    # добавление узла к указанному (родительскому) узлу
    def _add(self, value, node):
        if value < node.value:
            if node.left:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(value, node.right)
            else:
                node.right = Node(value)
    
    # получение узла по значению
    def find(self, value):
        if self.root:
            return self._find(value, self.root)
        else:
            return None

	# поиск узла (реализация)
    def _find(self, value, node):
        if value == node.value:
            return node
        elif (value < node.value and node.left):
            self._find(value, node.left)
        elif (value > node.value and node.right):
            self._find(value, node.right)

	# удаление дерева
    def delete_tree(self):
        self.root = None

	# вывод дерева
    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
    # вывод дерева (реализация)
    def _print_tree(self, node):
        """
        Iterative Inorder
        """
        if node:
            self._print_tree(node.left)
            print(f'{node.value} ')
            self._print_tree(node.right)

# класс узла дерева
class Node:
	# инициализация узла
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
# Комментарии ниже относятся только к реализации дерева с помощью iterative_preorder. 
# Если нет узла, то создать стэк и в стэк добавить значение пустого узла. Пока стэк не равен None, добавить узел в его начало  и показать пользователю. Если узел относится к правому(большему) узлу, то добавить его в конец стэка как правый узел. Если узел относится к левому(меньшему узлу), то добавить его в конец стэка как левый узел
def binary_tree():
    def iterative_preorder(node=None):
        if not node:
            return
        stack = []
        stack.append(node)
        while stack:
            node = stack.pop()
            visit(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def iterative_inorder(node=None):
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                visit(node)
                node = node.right

    def iterative_postorder(node=None):
        stack = []
        last_node_visited = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek_node = stack.pop(0)
                if peek_node.right and last_node_visited != peek_node.right:
                    node = peek_node.right
                else:
                    visit(peek_node)
                    last_node_visited = stack.pop()

    def level_order(root=None):
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            visit(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def visit(node):
        print(node.value)
    
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(5)
    tree.add(1)
    tree.add(2)
    tree.add(6)
    tree.add(7)

    input("Enter to continue...")
    # tree.print_tree()

    print("Iterative Preorder")
    iterative_preorder(tree.root)

    # print("Iterative Inorder")
    # iterative_inorder(tree.root)

    # print("iterative Postorder")
    # iterative_postorder(tree.root)

    # print("Level Order")
    # level_order(tree.root)

    # print(tree.find(3).value)
    # print(tree.find(10))


def math_calculation():
    print("""
    Программа вычисляет математические примеры с использованием мат.операций:
    "+" сложения,
    "-" вычитания,
    "*" умножения,
    "/" деления.
    А также расстановки приоритетов с использованием круглых скобок "(" и ")".
    Например:
    ( 25 + 13 ) * 16 / 5 - 11
    ( -25 + 13 ) * 5 / 2 + ( 12 + 3 ) / 3
    """)

    string = input("Введите математический пример: ")
    # Если мы ввели что угодно в поле ввода:
    if string:
        # Переменным stack и error присваиваются значение результата выполнения функции parse_expression, которой в качестве 
        # аргумента передали введёный текст
        stack, error = parse_expression(string)
        # Если в переменную stack ничего не записалось...
        if not stack:
            # ...выводится переменная error
            print(error)
        # Иначе, если в stack что-нибудь записалось, начинаются расчёты
        else:
            # stack обрабатывается функцией infix_to_postfix
            stack = infix_to_postfix(stack)
            print(f"Результат вычисления равен: {calc_postfix(stack)}")
    # Если мы не ввели ничего:
    else:
        print("Вы не ввели пример... Попробуйте снова...")


def parse_expression(string):
    # Создаётся пустой список stack
    stack = []
    # Если функция check_brackets(с аргументом string) возвращает True
    if check_brackets(string):
        # .split Разбивает строку на части, используя разделитель, и возвращает эти части списком.
        # Направление разбиения: слева направо.
        # В переменную stack записывается результат выполнения функции .split над введённой строкой.
        stack = string.split()
    # Иначе, это означает что введенный пример не прошёл проверку на скобки, о чем мы и сообщаем.
    else:
        return False, "Ошибка в примере, проблемы со скобками..."
    # Функция возвращает строку разбитую посимвольно в виде списка
    return stack, 'All OK'


def check_brackets(string):
    # Если у нас скобки раставлены правильно, то при выполнении циклов, список stack должен остаться пустым
    stack = []
    flag = True
    # для каждого символа в тексте:
    for symbol in string:
        # Если встречается открытая скобка
        if symbol == '(':
            # В список записывается открытая скобка
            stack.append(symbol)
        # Иначе, если встречается закрытая скобка...
        elif symbol == ')':
            # ...и что-то уже есть в списке ...
            if stack:
                # ... последняя записанная скобка в списке удаляется и возвращается в переменную bracket
                bracket = stack.pop()
                # Если из списка удалилась не открывающая скобка, значит список был уже пуст - цикл прерывается и выдается flag False
                if bracket != '(':
                    flag = False
                    break
            # Если в тексте встретилась закрывающая скобка, а в списке нет скобок вовсе - значит скобки расставлены не правильно 
            else:
                # В таком случае переменной flag тоже передается значение False
                flag = False
                break
    # Когда все циклы завершены, наш список stack должен остаться пустым
    if stack:
        flag = False
    # Если все правильно, то значение флага должно остаться True, что мы и возвращаем.
    return flag

# Функция расчётов
def infix_to_postfix(stack):
    postfix = []
    op_stack = []
    # Словарь приоритета, где у каждого ключа "в кавычках" есть значение от 1 до 3
    priority = {
        "(": 1,
        "-": 2,
        "+": 2,
        "/": 3,
        "*": 3
    }
    # Для каждого символа в веденном примере
    for item in stack:
        # Если это цифра...
        if is_digit(item):
            #...то эта цифра добавляется в список postfix
            postfix.append(item)
        # Если это открывающая скобка...
        elif item == '(':
            #... то эта скобка добавляется в список op_stack
            op_stack.append(item)
        # Если это закрывающая скобка...
        elif item == ')':
            # То создается переменная из удаленной скобки из списка op_stack
            top_item = op_stack.pop()
            # Пока эта скобка не открывающая
            while top_item != '(':
                # в список postfix записывается закрывающая скобка
                postfix.append(top_item)
                # а значению переменной top_item присваивается значение последнего удаленного символа из op_stack
                top_item = op_stack.pop()
        # Если это не скобка и не число:
        else:
            # Пока список op_stack больше или равен значению из словарая priority и пока значение вызванного ключа из словаря priority
            # больше или равно значению из словаря priority
            while op_stack and priority[op_stack[len(op_stack) - 1]] >= priority[item]:
                # В список postfix добавляется удаленный элемент из списка op_stack
                postfix.append(op_stack.pop())
            # после того, как цикл while завершился - в op_stack записывается значение символа (который не скобка)
            op_stack.append(item)
    # После того как мы разобрали каждый символ из примера, запускается этот цикл. Пока у нас есть хоть какое-нибдуь значение в списке
    # op_stack - эти значения переносятся в список postfix
    while op_stack:
        postfix.append(op_stack.pop())
    # После этого функция возвращает значения списка postfix. В работу вступает строка -
    # print(f"Результат вычисления равен: {calc_postfix(stack)}")
    return postfix

# в функцию в качестве аргумента поступает обработанный список stack
def calc_postfix(stack):
    # создается уже другой пустой список op_stack
    op_stack = []
    # для каждого элемента в списке
    for item in stack:
        # если это число:
        if is_digit(item):
            # в список добавляется целое значение числа
            op_stack.append(int(item))
        # Иначе:
        else:
            # берется переменная а из списка с конца
            a = op_stack.pop()
            # берется переменна b из списка с конца
            b = op_stack.pop()
            # Вычисляется пример по трем аргументам, так как item не число - значит он символ математической операции
            result = calc_simple(b, a, item)
            # результат записывается в список op_stack
            op_stack.append(result)
    # После вычисления возвращается последний элемент списка op_stack
    return op_stack.pop()

# Функция, которая определяет число, даже если оно отрицательное
def is_digit(number):
    if number.isdigit():
        return True
    elif number[0] == '-' and number[1:].isdigit():
        return True
    return False

# В зависимости от символа, выполняется определенная операция
def calc_simple(a, b, operation):
    oper_dict = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
        }
    return oper_dict.get(operation)


def main():
    while True:
        selector = {
            "1": binary_tree,
            "2": math_calculation,
        }
        next_step = input(
    """
    Выберите задачу.
    Обход дерева:           1
    Решение мат. примера:   2
    Выход:                  Enter
    """
        )
        if next_step:
            if selector.get(next_step):
                selector[next_step]()
            else:
                print("Повторите ввод...")
        else:
            print("Увидимся...")
            break        


if __name__ == "__main__":
    main()