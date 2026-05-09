# Detect duplicates lazily
# finds the first duplicate value in a list

# The list of numbers to check
nums = [1, 2, 3, 5, 2, 8]

# An empty set used to keep track of the numbers the program has 
#  already looked at
seen = set()

# next(,,,. None) - grabs the very first item that makes the condition True. 
# If the loop finishes without finding a duplicate, it returns None

dup = next(
    (n for n in nums if n in seen or seen.add(n)),
    None
)
"""
first check if n is already in the seen set

If n is in the set, the first part of the or is True, 
and the whole condition is True

If n is not in the set, it moves to the second part: seen.add(n). 
This adds the current number to the set and returns None 
(which counts as False), so the loop continues to the next number.
"""

print(dup)  # Output: 2