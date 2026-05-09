# Chained lazy pipelines

# calculate the sum of the squares of all even numbers from 0 up to 999,999

"""
While passing a large number into range(), we can place underscores between the digits to make the value easier to read

Python treats these underscores as invisible; 
they do not change the numerical value
"""

# Underscores in Numbers (as Digit Separators)

nums = range(1_000_000)    # Same as range(1000000)

#  use a generator expression to process the numbers efficiently 
# without creating a giant list in memory.
result = sum(       # Adds all those squares together
    n * n           # Squares each of those even numbers
    for n in nums   #  Loops through every number in that range
    if n % 2 == 0   # Filters the list to keep only even numbers
)

print(result)   # Output: 166666166667000000

# sum(x for x in items)