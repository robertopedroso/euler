from itertools import count

def evenlydivisible(n):
    """Returns whether n is divisible by [1, 20]"""
    drange = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # don't call xrange every time
    for i in drange:
        if n % i != 0: return False

    return True

if __name__ == "__main__":
    for i in count(20, 20): # start at 20 and step up by 20
        if evenlydivisible(i):
            print i
            break
