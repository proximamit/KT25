# left shift operator   <<

x = 3  # Binary: 0000 0011
result = x << 2  # Shift left by 2 positions

print(result)  # Output: 12 (Binary: 0000 1100)

""" 
Mathematically, shifting an integer left by n bits is equivalent to multiplying that integer by 2**n (for non-negative numbers). 

For example, 3 << 2 is the same as 3 * 2**2 
= 3 * 4 
= 12
"""
