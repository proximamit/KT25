
# Combinatorics (permutations & combinations) 
'''
Used to generate all possible arrangements or groupings required/useful for backtracking problems.
'''

import itertools

# Combinations: Selection of items where order doesn't matter
# Example: 2-item combinations from {1,2,3,4}

print(list(itertools.combinations([1, 2, 3, 4], 2)))
# Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# Permutations: Ordering of items where order matters
# Example: All 3-letter permutations of 'ABC'

print(list(itertools.permutations(['A', 'B', 'C'], 3)))
# Output: [('A', 'B', 'C'), ('A', 'C', 'B'), ...]
"""
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
"""
