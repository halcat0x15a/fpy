import operator

from functools import partial

class Placeholder(object):

    def __init__(self):
        for name in dir(operator):
            if name.startswith('__') and hasattr(getattr(operator, name), '__call__'):
                setattr(Placeholder, name, self.__getattr__(name))

    def __getattr__(self, name):
        return partial(operator.methodcaller, name)

_ = Placeholder()
