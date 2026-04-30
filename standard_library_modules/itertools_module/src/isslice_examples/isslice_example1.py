#  islice() (Slicing)
'''
Efficiently takes a slice of an iterator without converting it entirely to a list.
'''

import itertools
# Get the first 3 items from an infinite sequence
data = itertools.count(start=1, step=2)
print(list(itertools.islice(data, 3)))

# Output: [1, 3, 5]

# itertools.count(start, step): Generates numbers infinitely.
# Infinite iterators can cause TLE (Time Limit Exceeded)


"""
# Similarly
itertools.cycle(iterable): Repeats an iterable endlessly.
itertools.repeat(value): Repeats a value infinitely.
"""

#  To Prevent TLE with Infinite Iterators
# itertools.islice(): 
# The most efficient way to take a finite number of items from an 
# infinite source.
# break statement: Manually break the loop based on a condition.

# itertools.takewhile(): Collects elements while a condition is true.

# Take only the first 10 elements
for i in itertools.islice(itertools.count(3, 3), 10):
    print(i)
print("\n" * 3)
#  Break when value exceeds 15
for i in itertools.count(3, 3):                
    if i > 15:
        break
    print(i)
print("\n" * 2)
# Take values while they are <= 15
for i in itertools.takewhile(lambda x: x <= 15, itertools.count(3, 3)):
    print(i)