class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.next_node = None
        self.data = data


class LinkedList:
    """Класс для односвязного списка"""
    head = None
    tail = None

    def insert_beginning(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка
        """

        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка
        """

        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def to_list(self):
        """
        Метод озвращает список с данными, содержащимися в односвязном списке `LinkedList`
        """
        node = self.head
        if node is None:
            return str(None)

        ll_string = []
        while node:
            ll_string.append(node.data)
            node = node.next_node
        return ll_string

    def get_data_by_id(self, id):
        """
        Метод возвращает первый найденный в `LinkedList` словарь с ключом 'id',
        значение которого равно переданному в метод значению.
        Блок `try/except` перехвает ошибки `TypeError` и выводит сообщение
        'Данные не являются словарем или в словаре нет id.'
        """
        node = self.head
        if node is None:
            return str(None)

        while node:
            try:
                node = node.next_node
                if node.data['id'] == id:
                    return node.data
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')


    def __str__(self) -> str:
        """
        Вывод данных односвязного списка в строковом представлении
        """
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
