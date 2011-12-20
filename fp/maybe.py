from monad import Monad

class Maybe(Monad):

    @classmethod
    def pure(self, a):
        return Just(a)

    def bind(self, f):
        return Nothing

Nothing = Maybe()

class Just(Maybe):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Just) and other.value == self.value

    def __str__(self):
        return "Just({0})".format(self.value)

    def bind(self, f):
        return f(self.value)
