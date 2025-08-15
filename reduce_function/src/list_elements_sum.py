# Sum of all elements of a list

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)              # Output: 55
