class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        node.next_node = None
        if self.length == 0:
            # если список пуст, новый узел является головным и последним
            self.head = self.tail = node
        else:
            # иначе, найти последний узел
            tail = self.tail
            # добавить новый узел
            tail.next_node = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            nod = self.head.data
            self.head = self.head.next_node
            return nod

    def __str__(self):
        """
        Магический метод для строкового представления объекта
        """
        if self.head == None:
            return ""
        return f'{self.head.data}\n{self.head.next_node.data}\n{self.tail.data}'

