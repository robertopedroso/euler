from __future__ import division
from math import floor

def gauss(date, month, year):
    """Gaussian algorithm for computing the day of a week for a given date. Returns
    an integer in [0,6] where 0=Sunday and 6=Saturday."""
    if month == 1 or month == 2: year -= 1  # year-1 for Jan or Feb
    month = ((month + 9) % 12) + 1  # months shifted such that March is 1
    y, c = int(''.join(str(year)[-2:])), int(''.join(str(year)[:2]))

    return int((date + floor(2.6*month - 0.2) + y + floor(y/4) + floor(c/4) - (2*c)) % 7)

if __name__ == "__main__":
    count = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            if gauss(1, month, year) == 0: count += 1
    print count
