import operator

from functools import partial, reduce

class _(object):

    def __init__(self):
        for name in dir(operator):
            if name.startswith('__') and hasattr(getattr(operator, name), '__call__'):
                setattr(_, name, self.__getattr__(name))

    def __getattr__(self, name):
        return partial(operator.methodcaller, name)

_ = _()

def identity(a):
    return a

sum = partial(reduce, operator.add)
