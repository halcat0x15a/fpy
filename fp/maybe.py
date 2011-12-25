from fp.typeclass import Monad, Monoid, Iteratable

class Maybe(Monad, Monoid, Iteratable):

    def pure(self, a):
        return Just(a)

    def zero(self):
        return Nothing

class Nothing(Maybe):

    def bind(self, f):
        return Nothing

    def append(self, m):
        return m

    def __str__(self):
        return "Nothing"

    def __iter__(self):
        return iter(())

Nothing = Nothing()

class Just(Maybe):

    def __init__(self, value):
        self.value = value

    def bind(self, f):
        return f(self.value)

    def append(self, m):
        return self if Nothing == m else Just(self.value + m.value)

    def __eq__(self, other):
        return isinstance(other, Just) and other.value == self.value

    def __str__(self):
        return "Just({0})".format(self.value)

    def __iter__(self):
        yield self.value
