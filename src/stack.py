class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data


class Stack:
    """Класс для стека"""

    def __init__(self):
        """
        Конструктор класса Stack
        """
        self.top = None


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data, self.top)
        self.top = node


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is not None:
            nod = self.top.data
            self.top = self.top.next_node
            return nod


    def __str__(self):
        return f'{self.__class__.__name__}'


