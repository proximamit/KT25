# Find the maximum element

from functools import reduce

numbers = [10, 20, 5, 100, 50]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)               # Output: 100