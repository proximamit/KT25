# Old .format
print("{:.2f}".format(3.14159))

# New f-string
print(f"{3.14159:.2f}")

# : starts the formatting rule
# .2 means two numbers after the dot
# f means a float number

##  Padding Numbers with Leading Zeros
number = 42

# Pad to a total width of 5 characters
print(f"{number:05d}")  
# Output: 00042

"""
0: Specifies the padding character (zero).
5: Total length of the output string.
d: Stands for decimal integer.
"""

##  Formatting with Commas for Thousands
large_amount = 3212505000

# Format with commas
print(f"{large_amount:,}")  
# Output: 3,212,505,000


## Combining Both (Commas and Decimal Places)

price = 12500.756

# Add commas and round to 2 decimal places
print(f"{price:,.2f}") 