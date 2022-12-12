# is_empty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.

class Stack:
    def __init__(self):
        self.array = []

    def is_empty(self):
        return not bool(self.array)

    def push(self, element):
        self.array.append(element)

    def pop(self):
        return self.array.pop()

    def peek(self):
        return self.array[-1]

    def size(self):
        return len(self.array)


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())
