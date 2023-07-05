"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestStack(unittest.TestCase):

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 2})
        self.assertEqual(ll.head.data, {'id': 2})

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.tail.next_node, None)


    def test_str(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")


    def test_to_list(self):
        # Создаем и наполняем односвязный список
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        lst = ll.to_list()
        self.assertEqual(lst, [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}])
        user_data = ll.get_data_by_id(3)
        self.assertEqual(user_data, {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id(self):

        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        user_data = ll.get_data_by_id(2)
        self.assertEqual(user_data, {'id': 2, 'username': 'mosh_s'})





