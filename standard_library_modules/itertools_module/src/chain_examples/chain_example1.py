# chain() (Flattening)
'''
Flattens multiple iterables (lists, sets) into a single sequence efficiently.
'''

import itertools
list1 = [1, 2]
list2 = ['a', 'b']
# Combine lists without creating a new huge list in memory
print(list(itertools.chain(list1, list2)))
# Output: [1, 2, 'a', 'b']
