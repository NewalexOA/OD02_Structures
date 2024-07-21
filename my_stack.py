class Stack:
    def __init__(self):
        """
        Инициализирует пустой стек, используя список.

            Атрибуты:
            stack -- список для хранения элементов стека.
        """
        self.stack = []

    def push(self, item):
        """
        Добавляет элемент в верхнюю часть стека.

            Аргументы:
            item -- элемент, который нужно добавить в стек.
        """
        self.stack.append(item)

    def pop(self):
        """
        Удаляет и возвращает элемент из верхней части стека.

            Возвращает:
            Элемент, удаленный из верхней части стека.

            Вызывает исключение:
            Exception -- если стек пуст.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack.pop()

    def size(self):
        """
        Возвращает количество элементов в стеке.

            Возвращает:
            Количество элементов в стеке.

            Вызывает исключение:
            Exception -- если стек пуст.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return len(self.stack)

    def is_empty(self):
        """
        Проверяет, пуст ли стек.

            Возвращает:
            True, если стек пуст, иначе False.
        """
        return self.stack == []

    def peek(self):
        """
        Возвращает элемент из верхней части стека, не удаляя его.

            Возвращает:
            Элемент из верхней части стека.

            Вызывает исключение:
            Exception -- если стек пуст.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack[-1]

    def clear(self):
        """
        Очищает стек, удаляя все элементы.
        """
        self.stack = []

    def show(self):
        """
        Отображает все элементы стека.

            Вызывает исключение:
            Exception -- если стек пуст.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        print(self.stack)


# Пример использования класса Stack
s = Stack()
s.push(1)  # Добавляем элемент 1 в стек
s.push(2)  # Добавляем элемент 2 в стек
s.push(3)  # Добавляем элемент 3 в стек
s.show()  # Отображаем содержимое стека
# Output:
# [1, 2, 3]

print(s.pop())  # Удаляем и возвращаем верхний элемент стека (3)
# Output:
# 3

print(s.size())  # Возвращаем количество элементов в стеке
# Output:
# 2

print(s.is_empty())  # Проверяем, пуст ли стек
# Output:
# False

print(s.peek())  # Возвращаем верхний элемент стека без удаления (2)
# Output:
# 2

s.clear()  # Очищаем стек
s.show()  # Попытка отобразить содержимое стека вызывает исключение
# Output:
# Exception: Stack is empty
