"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)


    def test_push(self):
        stack = Stack()
        stack.push("datastr1")
        self.assertEqual(stack.top.data, "datastr1")


    def test_pop(self):
        stack = Stack()
        stack.push("datastr1")
        stack.pop()
        #stack.push("datastr2")
        self.assertEqual(stack.top, None)



