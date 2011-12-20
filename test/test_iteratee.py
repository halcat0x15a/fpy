from unittest import TestCase, main

from iteratee import *

class IterateeTest(TestCase):

    def test_input(self):
        self.assertNotEqual(Empty, EOF)

    def test_fmap(self):
        self.assertEqual(head().fmap2(lambda i: i + 10).enum([1, 2, 3]).run(), Just(11))

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
        pass

    def test_bind_(self):
        self.assertEqual((drop(0) >> peek()).enum([1, 2, 3]).run(), Just(1))
        self.assertEqual((drop(1) >> head()).enum([1, 2, 3]).run(), Just(2))
        self.assertEqual((peek() >> peek()).enum([1, 2, 3]).run(), Just(1))
        self.assertEqual((head() >> peek()).enum([1, 2, 3]).run(), Just(2))

    def test_file_lines(self):
        name = 'test.txt'
        self.assertEqual(head().file_lines(name).run(), Just('hello\n'))
        self.assertEqual(drop(2).bind_(head()).file_lines(name).run(), Just('python\n'))
        self.assertEqual(drop(1).bind_(length()).file_lines(name).run(), 2)

if __name__ == '__main__':
    main()
