def squaresum(n):
    """Returns the sum of the squares of the natural numbers [1, n]"""
    return sum(x * x for x in xrange(1, n+1))

def sumsquare(n):
    """Returns the square of the sum of the natural numbers [1, n]"""
    return sum(xrange(1, n+1)) ** 2

if __name__ == "__main__":
    # problem 6 asks for sumsquare - squaresum for [1..100]
    print sumsquare(100) - squaresum(100)
