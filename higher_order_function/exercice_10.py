from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda a, b: a + b,
    map(
        lambda x: x * 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)