from itertools import count


def is_evenly_divisible(number, rng):
    for d in rng:
        if number % d != 0:
            return False
    return True


def generate_evenly_divisible(max_divisor):
    r = range(3, max_divisor + 1)
    for n in count(max_divisor, max_divisor):
        if is_evenly_divisible(n, r):
            yield n


print next(generate_evenly_divisible(20))
