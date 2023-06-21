"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestStack(unittest.TestCase):

    def test_init(self):
        assert str(Queue()) == ""


    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next_node.data, "data2")
        self.assertEqual(queue.tail.data, "data3")
        self.assertEqual(queue.tail.next_node, None)


    def test_dequeue(self):
        # Создаем пустую очередь
        queue = Queue()

        # Добавляем данных в очередь
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        assert queue.dequeue() == 'data1'
        assert queue.dequeue() == 'data2'
        assert queue.dequeue() == 'data3'
        assert queue.dequeue() is None


    def test_str(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next_node.data, "data2")
        self.assertEqual(queue.tail.data, "data3")
        self.assertEqual(queue.tail.next_node, None)
        self.assertEqual(str(queue), "data1\ndata2\ndata3")