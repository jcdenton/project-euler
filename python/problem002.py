from itertools import ifilter


def fib(n):
    current, inc = 0, 1
    while current < n:
        yield current
        current, inc = inc, current + inc


print sum(ifilter(
    lambda i: i % 2 == 0,
    fib(4 * (10 ** 6))))
