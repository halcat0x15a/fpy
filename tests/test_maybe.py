from unittest import TestCase

from fp import _
from fp.maybe import *

class MaybeTest(TestCase):

    def test_str(self):
        self.assertEqual(str(Nothing), "Nothing")
        self.assertEqual(str(Just(1)), "Just 1")

    def test_pure(self):
        self.assertEqual(Maybe.pure(1), Just(1))

    def test_bind(self):
        self.assertEqual(Just(1) >= (lambda x: Just(x + 1)), Just(2))
        self.assertEqual(Just("python") >> Nothing, Nothing)
        self.assertEqual(Nothing >> Just(1), Nothing)

    def test_map(self):
        self.assertEqual(Just(1) > (_ + 1), Just(2))
        self.assertEqual(Nothing > (_ + 1), Nothing)

    def test_apply(self):
        self.assertEqual(Just(_ + 1) * Just(1), Just(2))
        self.assertEqual(Just(_ + 1) * Nothing, Nothing)
        self.assertEqual(Nothing * Just(1), Nothing)
