def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def binominal_coefficient(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


def paths(x, y=None):
    y = y or x
    return binominal_coefficient(x + y, x)


print paths(20)
