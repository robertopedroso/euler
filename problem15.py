from util import memoized

@memoized
def fac(n):
    """Returns the factorial of n"""
    if n == 1: return 1
    return n * fac(n-1)

def numpaths(a, b):
    """Returns the number of paths through a lattice from the origin to (a,b)"""
    return fac(a+b) / (fac(b) * fac(a)) # number of paths given by (a+b a)

if __name__ == "__main__":
    # problem asks for number of paths through a 20x20 grid
    print numpaths(20, 20)
