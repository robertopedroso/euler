import itertools

def euclid(n, m):
    """Given two integers n and m such that n > m, return the
    corresponding Pythagorean triple
    """
    return (n**2 - m**2, 2 * n * m, n**2 + m**2)

def triple_for_sum(s):
    """Returns the first Pythagorean triple whose add up to the given sum"""
    for n in itertools.count(2):
        for m in xrange(1, n):
            triple = euclid(n, m)
            if sum(triple) == s:
                return triple

if __name__ == "__main__":
    # problem 8 asks for a the product of the triplet whose sum is 1000
    triplet = triple_for_sum(1000)
    product = triplet[0] * triplet[1] * triplet[2]
    print product
