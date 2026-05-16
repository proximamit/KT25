import math

def climb_stairs(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2

    return int((phi**(n + 1) - psi**(n + 1)) / math.sqrt(5))

"""
Advantage

Very fast theoretically.

Disadvantage
Floating point precision issues
Less readable
"""

if __name__ == "__main__":
    n = int(input("Enter number of steps: "))
    print("Number of distinct ways:", climb_stairs(n))

