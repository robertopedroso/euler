def num_to_words(n):
    """Returns the english word representation of an integer n for n in [1,1000]
    Adapted from: http://stackoverflow.com/a/19193721
    """
    if n < 1 or n > 1000: raise ValueError("Only supports n in [1,1000]")
    if n == 1000: return "one thousand"
    
    base = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['', 'eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
            'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']

    words = []
    numstr = str(n)

    # figure out how many groups of 3 digits are in n
    # pad with 0s if needed to make all groups triples
    # convert back to an int list
    groups = ((len(numstr) + 2) / 3)
    num = [int(x) for x in numstr.zfill(groups * 3)]

    # iterate by 3s to cover groups
    for i in xrange(0, groups*3, 3):
        x, y, z = num[i], num[i+1], num[i+2]

        # hundreds place of group
        if x >= 1:
            words.append(base[x])
            words.append('hundred')

        # tens and ones places of group
        if x >= 1 and (y >= 1 or z >= 1):
            words.append('and')

        if y > 1:
            words.append(tens[y])
            if z >= 1: words.append(base[z])
        elif y == 1:
            if z >= 1: words.append(teens[z])
            else: words.append(tens[y])
        else:
            if z >= 1: words.append(base[z])

    return ' '.join(words)

def lettercount(s):
    """Returns the number of letters in s"""
    return len(s.replace(' ',''))

def numletters(n):
    """Returns the number of letters in the English word form of n in [1,1000]"""
    return lettercount(num_to_words(n))

if __name__ == "__main__":
    count = 0
    for i in xrange(1, 1001):
        count += numletters(i)
    print count

