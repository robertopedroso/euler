def gpf(n):
    """Performs optimized trial-division to find the greatest prime factor of n"""
    i = 2
    while i * i < n:
        while n % i == 0:
            n /= i
        i += 1
    
    return n

if __name__ == "__main__":
    n = 600851475143
    print gpf(n)
