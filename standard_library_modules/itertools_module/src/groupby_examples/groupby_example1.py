# groupby() (Data Grouping)
# Groups consecutive elements based on a key. 

from itertools import groupby

data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('A', 5)]
# Group by the first element of the tuple
for key, group in groupby(data, lambda x: x[0]):
    print(key, list(group))

# Output: 
"""
A [('A', 1), ('A', 2)]
B [('B', 3), ('B', 4)]
A [('A', 5)]
"""
