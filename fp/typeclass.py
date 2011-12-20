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

    def fmap(self, f):
        pass

    def fmap2(self, f):
        return self.fmap(lambda a: a.fmap(lambda b: f(b)))

class Apply(object):

    def apply(self, a):
        pass

class Applicative(Pure, Functor, Apply):

    def fmap(self, f):
        return self.pure(f).apply(self)

class Monad(Applicative, Bind):

    def fmap(self, f):
        return self.bind(lambda a: self.pure(f(a)))

    def apply(self, m):
        return self.bind(lambda k: m.fmap(lambda a: k(a)))
