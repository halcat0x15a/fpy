from typeclass import Monad

class Writer(Monad):

    def __init__(self, w, a):
        self.written = w
        self.over = a

    def pure(self, a):
        return Writer(self.written.zero(), a)

    def bind(self, f):
        k = f(self.over)
        return Writer(self.written + k.written, k.over)
