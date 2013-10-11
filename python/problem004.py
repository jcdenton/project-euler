from itertools import ifilter, product, starmap
from operator import mul


def is_palyndrome(n):
    return str(n) == str(n)[::-1]


print reduce(max, ifilter(
    is_palyndrome,
    starmap(mul, product(xrange(100, 1000), repeat=2))))
