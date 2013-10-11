from itertools import ifilter

from util import fib


print sum(ifilter(
    lambda i: i % 2 == 0,
    fib(4 * (10 ** 6))))
