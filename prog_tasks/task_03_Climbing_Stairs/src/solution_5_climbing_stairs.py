# using Memoization

# Using Python's built-in cache:

from functools import lru_cache

@lru_cache(None)
def climb_stairs(n):
    if n <= 2:
        return n

    return climb_stairs(n - 1) + climb_stairs(n - 2)

print(climb_stairs(5))

# Why this is good
'''

Elegant recursive style
Avoids repeated calculations
Python automatically stores computed results

This is also Dynamic Programming.
'''

if __name__ == "__main__":
    n = int(input("Enter number of steps: "))
    print("Number of distinct ways:", climb_stairs(n))
