class Graf(object):
    """
    Класс представляет собой простую реализацию неориентированного графа.
    """
    def __init__(self):
        self.graf = {}

    def add_node(self, node):
        """
        Добавляет узел в граф с пустым списком соседних узлов.

        Аргументы:
        node -- узел, который нужно добавить в граф.
        """
        self.graf[node] = []

    def add_edge(self, node1, node2):
        """
        Добавляет ребро между двумя узлами. Узлы должны существовать в графе.

        Аргументы:
        node1 -- первый узел.
        node2 -- второй узел.
        """
        self.graf[node1].append(node2)
        self.graf[node2].append(node1)

    def show(self):
        """
        Отображает граф в виде строк.
        Для каждого узла выводится узел и его соседи, разделенные стрелками '->'.
        """
        for node in self.graf:
            print(node, "->", " -> ".join(map(str, self.graf[node])))

    def clear(self):
        """
        Очищает граф, устанавливая словарь графа в пустой словарь.
        """
        self.graf = {}


# Пример использования класса Graf
g = Graf()
g.add_node("A")  # Добавляем узел 'A'
g.add_node("B")  # Добавляем узел 'B'
g.add_node("C")  # Добавляем узел 'C'
g.add_edge("A", "B")  # Добавляем ребро между 'A' и 'B'
g.add_edge("A", "C")  # Добавляем ребро между 'A' и 'C'
g.show()  # Отображаем граф

# Output:
# A -> B -> C
# B -> A
# C -> A
