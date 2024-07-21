class Node(object):
    """
    Класс для представления узла бинарного дерева.

        Атрибуты:
        value -- значение узла.
        left -- левый потомок узла (инициализируется как None).
        right -- правый потомок узла (инициализируется как None).
    """
    def __init__(self, key):
        """
        Инициализирует узел с заданным значением.
            Аргументы:
            key -- значение узла.
        """
        self.value = key
        self.left = None
        self.right = None


def insert(root, key):
    """
    Вставляет новый узел с заданным значением в бинарное дерево.
        Аргументы:
        root -- корневой узел дерева.
        key -- значение, которое будет вставлено в дерево.

    Возвращает:
        Корневой узел дерева после вставки нового узла.
    """
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# Пример использования
root = Node(10)  # Создаем корневой узел с значением 10
root = insert(root, 5)  # Вставляем узел с значением 5
root = insert(root, 15)  # Вставляем узел с значением 15
root = insert(root, 3)  # Вставляем узел с значением 3
root = insert(root, 7)  # Вставляем узел с значением 7
