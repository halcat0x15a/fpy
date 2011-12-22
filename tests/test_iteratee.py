from unittest import TestCase

from fp import _
from fp.iteratee import *

class IterateeTest(TestCase):

    def test_input(self):
        self.assertNotEqual(Empty, EOF)

    def test_map(self):
        self.assertEqual(head().map2(_ + 10).enum([1, 2, 3]).run(), Just(11))

    def test_head(self):
        self.assertEqual(head().enum([1, 2, 3]).run(), Just(1))
        self.assertEqual(head().enum([]).run(), Nothing)

    def test_peek(self):
        self.assertEqual(peek().enum([1, 2, 3]).run(), Just(1))
        self.assertEqual(peek().enum([]).run(), Nothing)

    def test_drop(self):
        self.assertEqual(drop(1).enum([1, 2, 3]).run(), ())

    def test_length(self):
        self.assertEqual(length().enum([1, 2, 3]).run(), 3)
        self.assertEqual(length().enum([]).run(), 0)

    def test_bind(self):
        self.assertEqual((drop(0) >> peek()).enum([1, 2, 3]).run(), Just(1))
        self.assertEqual((drop(1) >> head()).enum([1, 2, 3]).run(), Just(2))
        self.assertEqual((peek() >> peek()).enum([1, 2, 3]).run(), Just(1))
        self.assertEqual((head() >> peek()).enum([1, 2, 3]).run(), Just(2))

    def test_file_lines(self):
        name = 'tests/test.txt'
        self.assertEqual(head().file_lines(name).run(), Just('hello\n'))
        self.assertEqual((drop(2) >> head()).file_lines(name).run(), Just('python\n'))
        self.assertEqual((drop(1) >> length()).file_lines(name).run(), 2)
