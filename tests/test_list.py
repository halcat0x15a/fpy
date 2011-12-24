from unittest import TestCase

from fp.list import *

class ListTest(TestCase):

    def test_str(self):
        self.assertEqual(str(Nil), 'Nil')
        self.assertEqual(str(List(1, 2, 3)), 'Cons(1, Cons(2, Cons(3, Nil)))')

    def test_len(self):
        self.assertEqual(len(Nil), 0)
        self.assertEqual(len(List(1, 2, 3)), 3)

    def test_iter(self):
        i = iter(List(3, 2, 1))
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 1)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_eq(self):
        self.assertEqual(Nil, Nil)
        self.assertNotEqual(Nil, List(1))        
        self.assertEqual(List(1, 2), List(1, 2))
        self.assertNotEqual(List(1, 2), Nil)
        self.assertNotEqual(List(1, 2), List(1, 3))

    def test_bind(self):
        self.assertEqual(List(1, 2, 3) >= (lambda x: List(x, x + 1)), List(1, 2, 2, 3, 3, 4))
        self.assertEqual(Nil >= (lambda x: List(x, x + 1)), Nil)

    def test_add(self):
        self.assertEqual(List(1, 2) + List(3), List(1, 2, 3))
        self.assertEqual(Nil + List(3), List(3))
        self.assertEqual(Nil + Nil, Nil)
