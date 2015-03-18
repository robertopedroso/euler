def ismultiple(n):
    """Returns true if n is a multiple of 3 or 5"""
    return n % 3 == 0 or n % 5 == 0

if __name__ == "__main__":
    multiples = [n for n in xrange(1, 1000) if ismultiple(n)]
    print sum(multiples)
