def ispalindrome(n):
    """Returns true if an int n, considered as a string, is a palindrome."""
    n = str(n)
    a, b = n[:len(n)/2], n[len(n)/2:]
    if len(a) != len(b): b = b[1:] # remove 'middle' number, if there is one
    return a[::-1] == b

if __name__ == "__main__":
    largest = 0
    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            result = i * j
            if ispalindrome(result):
                largest = max(result, largest)

    print largest
