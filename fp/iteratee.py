from functools import partial

from monad import Monad

from maybe import *

class Input(object):

    def input(self, el, empty, eof):
        if self == Empty:
            return empty
        elif self == EOF:
            return eof
        else:
            return el(self)

class El(Input):

    def __init__(self, e):
        self.e = e

Empty = Input()

EOF = Input()

class IterV(Monad):

    @classmethod
    def pure(self, a):
        return Done(a, Empty)

    def file_lines(self, path):
        f = open(path)
        try:
            return self._handle(f)
        finally:
            f.close()

class Done(IterV):

    def __init__(self, a, i):
        self.a = a
        self.i = i

    def enum(self, i):
        return self

    def run(self):
        return self._maybe()

    def _maybe(self):
        return self.a

    def bind(self, f):
        return f(self.a)._bind(self.i)

    def _bind(self, i):
        return Done(self.a, i)

    def _handle(self, f):
        return self

class Cont(IterV):

    def __init__(self, k):
        self.k = k

    def enum(self, i):
        if len(i) == 0:
            return self
        else:
            x = i[0]
            xs = i[1:]
            return self.k(El(x)).enum(xs)

    def run(self):
        return self.k(EOF)._maybe()

    def _maybe(self):
        raise Exception()

    def bind(self, f):
        return Cont(lambda i: self.k(i).bind(f))

    def _bind(self, i):
        return self.k(i)

    def _handle(self, f):
        line = f.readline()
        if line:
            return self.k(El(line))._handle(f)
        else:
            return self

def head():
    def step(i):
        return i.input(el = lambda el: Done(Just(el.e), Empty), empty = Cont(step), eof = Done(Nothing, EOF))
    return Cont(step)

def peek():
    def step(i):
        return i.input(el = lambda el: Done(Just(el.e), el), empty = Cont(step), eof = Done(Nothing, EOF))
    return Cont(step)

def drop(n):
    if n == 0:
        return Done((), Empty)
    else:
        def step(i):
            return i.input(el = lambda _: drop(n - 1), empty = Cont(step), eof = Done((), EOF))
        return Cont(step)

def length():
    def step(acc, i):
        return i.input(el = lambda _: Cont(partial(step, acc + 1)), empty = Cont(partial(step, acc)), eof = Done(acc, EOF))
    return Cont(partial(step, 0))
