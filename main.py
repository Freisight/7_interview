# Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок.
# Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга.

# Задание 1

class Stack():
    def __init__(self):
        self.main_stack = []

    # isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        if self.main_stack == []:
            return True
        else:
            return False

    # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, new_element):
        self.main_stack.insert(0, new_element)
        pass

    # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        if self.isEmpty() is False:
            return self.main_stack.pop(0)
        else:
            return False
    # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        if self.isEmpty() is False:
            return self.main_stack[0]
        else:
            return False

    # size - возвращает количество элементов в стеке.
    def size(self):
        return len(self.main_stack)


# Задание 2
# Программа ожидает на вход строку со скобками. На выход сообщение: "Сбалансированно", если строка корректная, и "Несбалансированно", если строка составлена неверно.

def check(str):
    # Сразу отсекаем незакрытые скобки.
    if '(]' in str or '[)' in str or '[}' in str or '{]' in str or '(}' in str or '{)' in str:
        return 'Несбалансированно'

    # Далее полученные строки преобразуем в список и работаем с ним.
    get_list = list(str)

    # Создаем экземпляры стеков
    # {}
    curly_braces = Stack()

    # ()
    parenthesis = Stack()

    # []
    square_braces = Stack()

    # Проходим по списку
    for element in get_list:

        # Добавляем если скобка открыта
        if element == '(':
            parenthesis.push(element)

        # Удаляем если скобка закрыта
        elif element == ')':
            # Если в стеке нечего удалять значит закрытых больше и это уже не корректно возвращаем False
            if parenthesis.peek() is False:
                return 'Несбалансированно'
            # удаляем если скобка закрыта
            else:
                parenthesis.pop()

        # Далее аналогично
        elif element == '[':
            square_braces.push(element)

        elif element == ']':
            if square_braces.peek() is False:
                return 'Несбалансированно'
            else:
                square_braces.pop()

        # Далее аналогично
        elif element == '{':
            curly_braces.push(element)

        elif element == '}':
            if curly_braces.peek() is False:
                return 'Несбалансированно'
            else:
                curly_braces.pop()

    # Переборка стеков.
    if parenthesis.size() == 0 and square_braces.size() == 0 and curly_braces.size() == 0:
        return 'Сбалансированно'
    else:
        return False


if __name__ == '__main__':
    # Сбалансированные  последовательности:
    a = '(((([{}]))))'
    b = '[([])((([[[]]])))]'
    c = '{()}'
    d = '{{[()]}}'
    
    # Несбалансированные последовательности:
    e = '}{}'
    f = '{{[(])]}}'
    g = '[[{())}]'

    print(f'a - {check(a)}')
    print(f'b - {check(b)}')
    print(f'c - {check(c)}')
    print(f'd - {check(d)}')
    print(f'e - {check(e)}')
    print(f'f - {check(f)}')
    print(f'g - {check(g)}')