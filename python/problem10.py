from itertools import count
from math import sqrt

def isprime(n):
    """Returns True/False depending on whether n is prime"""
    if n % 2 == 0: return False
    for i in xrange(3, int(sqrt(n))+1, 2):
        if n % i == 0: return False
    return True

def genprimes():
    """A generator that generates primes by simply iterating and checking"""
    for n in count(5, 2):
        if isprime(n): yield n

if __name__ == "__main__":
    sieve = genprimes()
    primesum = 5 # since genprimes() ignores the first two primes, intiial sum = 5
    nextprime = next(sieve)
    while nextprime < 2000000:
        primesum += nextprime
        nextprime = next(sieve)

    print primesum
