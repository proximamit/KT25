# product() (Cartesian Product)
"""
Replaces nested for-loops, often used for grid searches.
"""

import itertools
# Example: All pairings of ranks and suits
ranks = ['A', 'K']
suits = ['H', 'S']
print(list(itertools.product(ranks, suits)))
# Output: [('A', 'H'), ('A', 'S'), ('K', 'H'), ('K', 'S')]
