"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        self.assertEqual(stack.str, [])

    def test_push(self):
        stack = Stack()
        stack.push("datastr1")
        self.assertEqual(stack.top.data, "datastr1")
        self.assertEqual(len(stack.str), 1)
