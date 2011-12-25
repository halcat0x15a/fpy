from fp.typeclass import *

class Maybe(Monad, Monoid, Iteratable, Equal, Show):

    def pure(self, a):
        return Just(a)

    def zero(self):
        return Nothing

class Nothing(Maybe):

    def bind(self, f):
        return Nothing

    def append(self, m):
        return m

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

    def __iter__(self):
        yield self.value
