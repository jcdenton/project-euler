from util import primes


def first_prime_factor(n):
    for prime in primes():
        if n % prime == 0:
            return prime


def prime_factors(n):
    prime = first_prime_factor(n)
    if prime == n:
        return [n]
    else:
        result = prime_factors(n / prime)
        result.append(prime)
        return result


print reduce(max, prime_factors(600851475143))
