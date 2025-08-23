"""
Given a list of numbers in which some numbers occur multiple times
Create a dictionary with the keys as the numbers from the list thus removing duplicates 
and the value of the key should be
the number of times the number occurs in the list
"""

'''
For example, for the input nums, the output is a dictionary as shown.
nums = [1, 2, 2, 3, 4, 3, 1, 1, 5]
output = {1: 3, 2: 2, 3: 2, 4: 1, 5: 1}
'''
# The goal is to count how many times each number appears in that list.

from collections import Counter

nums = [1, 2, 2, 3, 4, 3, 1, 1, 5]

# Use Counter to count occurrences
frequency_dict = Counter(nums)

# Print the result
print(frequency_dict)

# For output strictly as a regular dictionary (not a Counter object)
print(dict(frequency_dict))
