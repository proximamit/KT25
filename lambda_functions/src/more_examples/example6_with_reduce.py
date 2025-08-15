# Multiply all the numbers in a list 

from functools import reduce 

nums = [ 1, 2, 3, 4, 5, 6]
# Product of all the numbers in a given list
product = reduce(lambda x, y : x * y, nums)
print(product)                              # Output: 24