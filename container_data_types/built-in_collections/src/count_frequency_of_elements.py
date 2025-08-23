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

nums = [1, 2, 2, 3, 4, 3, 1, 1, 5]

# Create an empty dictionary to store frequencies
frequency_dict = {}

# Loop through each number in the list
for num in nums:
    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1

# Print the result
print(frequency_dict)
