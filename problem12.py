import itertools

def numdivisors(n):
    """Returns the number of divisors for n"""
    factors, factor = {}, 2
    while n > 1:
        if not n % factor:
            factors[factor] = factors.get(factor, 0) + 1
            n /= factor
        else:
            factor += 1

    total = 1
    for key in factors:
        total *= factors[key] + 1
    return total

def trianglenum():
    """Generator that returns sequential triangle numbers"""
    for i in itertools.count(1, 1):
        yield (i * (i + 1)) / 2

if __name__ == "__main__":
    for n in trianglenum():
        if numdivisors(n) >= 500:
            print n
            break
