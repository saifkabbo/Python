numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce

sum_numbers=reduce(lambda a,b:a+b,numbers)

print(sum_numbers)