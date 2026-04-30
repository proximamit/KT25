# Generate all subsets (Power Set)

from itertools import combinations

def subsets(nums):
    res = []
    for r in range(len(nums)+1):
        res.extend(combinations(nums, r))
    return res

print(subsets([1,2,3]))
