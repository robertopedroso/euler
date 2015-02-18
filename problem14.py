def collatz(n, count=1):
    """Returns the length of the collatz sequence spanning [n,1]"""
    while n > 1:
        count += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return count

if __name__ == "__main__":
    n, clen = 0, 0
    for i in xrange( 1000000):
        print i
        c = collatz(i)
        if c > clen:
            n, clen = i, c

    print n, clen
