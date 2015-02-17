from util import memoized
from itertools import count

@memoized
def fib(n):
    """Returns the nth number in the Fibonacci sequence"""
    if n in (0, 1): return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    sum = 0

    for n in count(1, 1):
        result = fib(n)
        if result > 4000000: break

        if result % 2 == 0: sum += result

    print sum
