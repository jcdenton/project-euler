from collections import deque
from itertools import takewhile, imap
from operator import itemgetter


def primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


print deque(
    imap(itemgetter(1),
         takewhile(lambda (i, v): i < 10001, enumerate(primes()))),
    maxlen=1).pop()
