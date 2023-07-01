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
