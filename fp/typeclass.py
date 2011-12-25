from fp import identity

class Equal(object):

    def __eq__(self, other):
        return isinstance(other, self.__class__) and hasattr(other, '__dict__') and self.__dict__ == other.__dict__

class Show(object):

    def __str__(self):
        values = self.__dict__.values()
        def comma(a, b):
            return '{0}, {1}'.format(a, b)
        return self.__class__.__name__ + ('' if len(values) == 0 else '({0})'.format(reduce(comma, map(str, values))))

class Pure(object):

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

    def zero(self):
        pass

class Semigroup(object):

    def append(self, m):
        pass

    def __add__(self, m):
        return self.append(m)

class Monoid(Zero, Semigroup):
    pass

class Iteratable(object):

    def __iter__(self):
        pass

    def __len__(self):
        return reduce(lambda a, _: a + 1, iter(self), 0)

    def __getitem__(self, i):
        return islice(iter(self), start=i)
