from unittest import TestCase

from fp import sum
from fp.writer import *
from fp.list import List

class WriterTest(TestCase):

    def test_bind(self):
        w = Writer('Hello', 100) >= (lambda x: Writer('World', x + 100))
        self.assertEqual(w.written, 'HelloWorld')
        self.assertEqual(w.over, 200)

    def test_map(self):
        w = Writer(List('python'), 10) > (lambda x: x * 2)
        self.assertEqual(sum(w.written), 'python')
        self.assertEqual(w.over, 20)
