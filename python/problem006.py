def sum_square_diff(max_number):
    numbers = xrange(1, max_number + 1)
    return sum(numbers) ** 2 - sum(map(lambda n: n ** 2, numbers))


print sum_square_diff(100)
