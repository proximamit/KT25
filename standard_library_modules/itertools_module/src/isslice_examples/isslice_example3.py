from itertools import islice

nums = range(10)
print(list(islice(nums, 2, 8, 2)))
# [2, 4, 6]