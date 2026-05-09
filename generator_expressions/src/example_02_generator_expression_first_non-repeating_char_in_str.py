# Write a Python one-liner that finds the first non-repeating character in a string 
# 
# (case-insensitive)

"""
Python one-liner to :

Convert the string to lowercase.

Use a generator to find characters that appear only once.

Use next() to grab the first such character.

Print it, or print None if none is found.
"""

s = "Swiss"
print(next((c for c in s.lower() if s.lower().count(c) == 1), None))

# s.lower() - To make the string lowercase (for case-insensitive)

# To create a generator that yields characters appearing only once
# (c for c in s.lower() if s.lower().count(c) == 1) 

# next(..., None) returns the first such character, or None if all characters repeat

# Case-sensitive 

# to respect case (i.e. 'S' not equal to 's')
print(next((c for c in s if s.count(c) == 1), None))

# c for c in s
# Loops through each character c in the string

# s.count(c) == 1
# Check if this character appear only once
# If yes, it yields (returns) that character


# next(..., None)
# This function takes two arguments

# next(iterator, default)
## It returns the first item from the generator
## If the generator is empty (i.e., no non-repeating characters), it returns None
