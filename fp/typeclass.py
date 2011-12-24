from fp import identity

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

    def join(self):
        return self.bind(identity)

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

class Zero(object):

    @classmethod
    def zero(self):
        pass

class Semigroup(object):

    def __add__(self, m):
        pass

class Monoid(Zero, Semigroup):
    pass

class Iteratable(object):

    def __iter__(self):
        pass

    def __len__(self):
        return reduce(lambda a, _: a + 1, iter(self), 0)

    def __getitem__(self, i):
        return islice(iter(self), start=i)
