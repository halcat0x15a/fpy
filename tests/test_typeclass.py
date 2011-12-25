from unittest import TestCase

from fp import _
from fp.maybe import Just
from fp.list import List

class TypeClassTest(TestCase):

    def test_join(self):
        self.assertEqual(Just(Just(1)).join(), Just(1))
        self.assertEqual(List([List([1, 2]), List([3, 4])]).join(), List([1, 2, 3, 4]))

    def test_map2(self):
        self.assertEqual(Just(Just(100)).map2(_ + 50), Just(Just(150)))
        self.assertEqual(List([List([1, 2]), List([3, 4])]).map2(_ + 1), List([List([2, 3]), List([4, 5])]))
