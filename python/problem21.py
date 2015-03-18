def sumdivisors(n):
    """Returns the sum of the proper divisors of n"""
    return sum([x for x in xrange(1, n) if n % x == 0])

if __name__ == "__main__":
    amicablenums = set()
    for n in xrange(1, 10000):
        if n in amicablenums: continue # no repeats
        x = sumdivisors(n)
        # we have to check that n != x because some numbers under 10,000
        # are such that n = sumdivisors(n)... [6, 28, 496, 8128]
        if n == sumdivisors(x) and n != x: amicablenums.update([n,x])
    print sum(amicablenums)
