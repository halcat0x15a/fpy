from unittest import TestCase

from fp.maybe import *

class MaybeTest(TestCase):

    def test_str(self):
        self.assertEqual(str(Nothing), 'Nothing')
        self.assertEqual(str(Just(1)), 'Just(1)')

    def test_bind(self):
        self.assertEqual(Just(1) >= (lambda x: Just(x + 1)), Just(2))
        self.assertEqual(Just('python') >> Nothing, Nothing)
        self.assertEqual(Nothing >> Just(1), Nothing)

    def test_eq(self):
        self.assertEqual(Nothing, Nothing)
        self.assertNotEqual(Nothing, Just(1))
        self.assertEqual(Just(1), Just(1))
        self.assertNotEqual(Just(1), Nothing)

    def test_add(self):
        self.assertEqual(Nothing + Nothing, Nothing)
        self.assertEqual(Nothing + Just(1), Just(1))
        self.assertEqual(Just(1) + Nothing, Just(1))
        self.assertEqual(Just(3) + Just(2), Just(5))

    def test_iter(self):
        i = iter(Just(5))
        self.assertEqual(next(i), 5)
        self.assertRaises(StopIteration, lambda: next(i))
        self.assertRaises(StopIteration, lambda: next(iter(Nothing)))
