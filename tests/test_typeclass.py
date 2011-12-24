from unittest import TestCase

from fp.maybe import Just
from fp.list import List

class TypeClassTest(TestCase):

    def test_join(self):
        self.assertEqual(Just(Just(1)).join(), Just(1))
        self.assertEqual(List(List(1, 2), List(4, 5)).join(), List(1, 2, 3, 4))
