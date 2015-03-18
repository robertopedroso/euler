from util import memoized

@memoized
def fac(n):
    """Returns the factorial of n"""
    if n == 1: return 1
    return n * fac(n-1)

def sumdigits(n):
    """Returns the sum of the digits in n"""
    digits = [int(x) for x in str(n)]
    return reduce(lambda x, y: x + y, digits)

if __name__ == "__main__":
    # problem 20 asks for the sum of the digits of 100!
    print sumdigits(fac(100))
