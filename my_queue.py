class Queue:
    def __init__(self):
        """
        Инициализирует пустую очередь, используя список.

            Атрибуты:
            queue -- список для хранения элементов очереди.
        """
        self.queue = []

    def enqueue(self, item):
        """
        Добавляет элемент в конец очереди.

            Аргументы:
            item -- элемент, который нужно добавить в очередь.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Удаляет и возвращает элемент из начала очереди.

            Возвращает:
            Элемент, удаленный из начала очереди.

            Вызывает исключение:
            Exception -- если очередь пуста.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue.pop(0)

    def size(self):
        """
        Возвращает количество элементов в очереди.

            Возвращает:
            Количество элементов в очереди.
        """
        return len(self.queue)

    def is_empty(self):
        """
        Проверяет, пуста ли очередь.

            Возвращает:
            True, если очередь пуста, иначе False.
        """
        return self.queue == []

    def peek(self):
        """
        Возвращает элемент из начала очереди, не удаляя его.

            Возвращает:
            Элемент из начала очереди.

            Вызывает исключение:
            Exception -- если очередь пуста.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[0]

    def clear(self):
        """
        Очищает очередь, удаляя все элементы.
        """
        self.queue = []

    def show(self):
        """
        Отображает все элементы очереди.

            Вызывает исключение:
            Exception -- если очередь пуста.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        print(self.queue)


# Пример использования класса Queue
q = Queue()
q.enqueue(1)  # Добавляем элемент 1 в очередь
q.enqueue(2)  # Добавляем элемент 2 в очередь
q.enqueue(3)  # Добавляем элемент 3 в очередь
q.show()  # Отображаем содержимое очереди
# Output:
# [1, 2, 3]

print(q.dequeue())  # Удаляем и возвращаем первый элемент очереди (1)
# Output:
# 1

print(q.size())  # Возвращаем количество элементов в очереди
# Output:
# 2

print(q.is_empty())  # Проверяем, пуста ли очередь
# Output:
# False

print(q.peek())  # Возвращаем первый элемент очереди без удаления (2)
# Output:
# 2

q.clear()  # Очищаем очередь
q.show()  # Попытка отобразить содержимое очереди вызывает исключение
# Output:
# Exception: Queue is empty
