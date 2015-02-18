import collections
import functools
import itertools

class memoized(object):
    """Decorator that caches a function's return values. Returns result
    from the cache if called with the same arguments again.

    Based on: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        # unhashable means uncacheable
        if not isinstance(args, collections.Hashable):
            return self.func(*args)

        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        """Return the decorated function's docstrong"""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods"""
        return functools.partial(self.__call__, obj)

def nth(iterable, n, default=None):
    """Returns the nth item of an iterable, else a default value
    From itertools recipes: https://docs.python.org/2/library/itertools.html
    """
    return next(itertools.islice(iterable, n, None), default)

def sumdigits(n):
    """Returns the sum of the digits of n"""
    digits = [int(x) for x in str(n)]
    return reduce(lambda x, y: x + y, digits)
