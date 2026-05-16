# Brute Force Recursion (Not Efficient)

def climb_stairs(n):
    if n <= 2:
        return n

    return climb_stairs(n - 1) + climb_stairs(n - 2)

# Problem 
'''
Very slow because of repeated calculations.
'''

if __name__ == "__main__":
    n = int(input("Enter number of steps: "))
    print("Number of distinct ways:", climb_stairs(n))
