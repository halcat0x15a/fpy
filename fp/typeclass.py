class Pure(object):

    @classmethod
    def pure(self, a):
        pass

class Bind(object):

    def bind(self, f):
        pass

    def __ge__(self, f):
        return self.bind(f)

    def bind_(self, a):
        return self.bind(lambda _: a)

    def __rshift__(self, a):
        return self.bind_(a)

class Functor(object):

    def map(self, f):
        pass

    def __gt__(self, f):
        return self.map(f)

    def map2(self, f):
        return self.map(lambda a: a.map(lambda b: f(b)))

class Apply(object):

    def apply(self, a):
        pass

    def __mul__(self, a):
        return self.apply(a)

class Applicative(Pure, Functor, Apply):

    def map(self, f):
        return self.pure(f).apply(self)

class Monad(Applicative, Bind):

    def map(self, f):
        return self.bind(lambda a: self.pure(f(a)))

    def apply(self, m):
        return self.bind(lambda k: m.map(lambda a: k(a)))
