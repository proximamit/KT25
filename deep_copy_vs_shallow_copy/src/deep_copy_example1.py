"""
Deep Copy - Concept
The outer object is copied, and all nested objects inside it are recursively copied

The deepcopy function copies not just the outer list, but also the inner lists [1, 2] and [3, 4]. 
So, the original list is entirely unaffected by changes made to the deep copy.

"""

import copy

# Original list with nested mutable objects
original = [[1, 2], [3, 4]]
print("Original:", original)  # [[1, 2], [3, 4]]

# Creating a deep copy
deep_copy = copy.deepcopy(original)

# Modify an element in the nested list inside the deep copy
deep_copy[0][0] = 95

# Now, only the deep copy reflects the change, not the original
print("Deep Copy:", deep_copy)  # [[95, 2], [3, 4]]
print("Original:", original)  # [[1, 2], [3, 4]]
