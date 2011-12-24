from fp.typeclass import Monad, Monoid

class Maybe(Monad, Monoid):

    @classmethod
    def pure(self, a):
        return Just(a)

    @classmethod
    def zero(self):
        return Nothing

class Nothing(Maybe):

    def bind(self, f):
        return Nothing

    def __add__(self, m):
        return m

    def __str__(self):
        return "Nothing"

Nothing = Nothing()

class Just(Maybe):

    def __init__(self, value):
        self.value = value

    def bind(self, f):
        return f(self.value)

    def __add__(self, m):
        return self if Nothing == m else Just(self.value + m.value)

    def __eq__(self, other):
        return isinstance(other, Just) and other.value == self.value

    def __str__(self):
        return "Just({0})".format(self.value)
