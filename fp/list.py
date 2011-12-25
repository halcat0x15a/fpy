from operator import eq
from typeclass import *

class List(Monad, Monoid, Iteratable, Equal, Show):

    def pure(self, a):
        return Cons(a)

    def zero(self):
        return Nil

class Nil(List):

    def bind(self, f):
        return Nil

    def append(self, m):
        return m

    def __iter__(self):
        return iter(())

Nil = Nil()

class Cons(List):

    def __init__(self, head, tail=Nil):
        self.head = head
        self.tail = tail

    def bind(self, f):
        return f(self.head).append(self.tail.bind(f))

    def append(self, m):
        return Cons(self.head, self.tail + m)

    def __iter__(self):
        yield self.head
        for a in iter(self.tail):
            yield a

def List(a):
    if len(a) == 0:
        return Nil
    else:
        t = a[1:]
        return Cons(a[0], Nil if len(t) == 0 else List(t))
