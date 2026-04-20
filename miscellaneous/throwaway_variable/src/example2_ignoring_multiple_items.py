# We use the asterisk (*_) to catch and discard all remaining values in a sequence. 
# This is a common practice for unpacking collections.

# Keep only the first value, discard the rest
head, *_ = [1, 2, 3, 4, 5]
print(head)  # Output: 1


values = (1, 2, 3, 4, 5)

a, _, _, d, _ = values
print(a, d)  # 1 4


numbers = [1, 2, 3, 4, 5]

first, *_, last = numbers
print(first, last)  # 1 5
# Here _ absorbs the middle values.
