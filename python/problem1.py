from itertools import ifilter


print sum(ifilter(
    lambda i: any(i % divisor == 0 for divisor in (3, 5)),
    xrange(1000)))
