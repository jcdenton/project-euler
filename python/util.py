def fib(n):
    current, inc = 0, 1
    while current < n:
        yield current
        current, inc = inc, current + inc


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
