from operator import eq
from typeclass import Monad, Monoid, Iteratable

class List(Monad, Monoid, Iteratable):

    def pure(self, a):
        return Cons(a)

    def zero(self):
        return Nil

class Nil(List):

    def bind(self, f):
        return Nil

    def __add__(self, m):
        return m

    def __str__(self):
        return 'Nil'

    def __iter__(self):
        return iter([])

Nil = Nil()

class Cons(List):

    def __init__(self, head, tail=Nil):
        self.head = head
        self.tail = tail

    def bind(self, f):
        return f(self.head) + self.tail.bind(f)

    def __add__(self, m):
        return Cons(self.head, self.tail + m)

    def __str__(self):
        return 'Cons({0}, {1})'.format(str(self.head), str(self.tail))

    def __eq__(self, other):
        return isinstance(other, Cons) and self.head == other.head and self.tail == self.tail

    def __iter__(self):
        yield self.head
        for a in iter(self.tail):
            yield a

def List(*a):
    if len(a) == 0:
        return Nil
    else:
        t = a[1:]
        return Cons(a[0], Nil if len(t) == 0 else List(*t))
