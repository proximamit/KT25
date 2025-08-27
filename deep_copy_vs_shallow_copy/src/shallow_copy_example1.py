"""
Concept:

When we perform a shallow copy, 
the outer list is copied, but the inner lists [1, 2] and [3, 4] are not copied. 
They are still references to the same objects as in the original list. 
Changing the inner list in the shallow copy affects the original list as well.

"""


import copy

# Original list with nested mutable objects
original = [[1, 2], [3, 4]]
print("Original:", original)  # Output: Original: [[1, 2], [3, 4]]

# Creating a shallow copy
shallow_copy = copy.copy(original)

# Modify an element in the nested list inside the shallow copy
shallow_copy[0][0] = 99

# Now, both original and shallow_copy will reflect the change
print("Shallow Copy:", shallow_copy)  #  Output: [[99, 2], [3, 4]]
print("Original:", original)  #  Output: [[99, 2], [3, 4]]
