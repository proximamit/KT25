def climb_stairs(n):
    # Base cases
    if n <= 2:
        return n

    # Variables to store previous two results
    first = 1
    second = 2

    # Calculate ways from step 3 to n
    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second

if __name__ == "__main__":
    # Input from user
    n = int(input("Enter number of steps: "))

    # Output result
    print("Number of distinct ways:", climb_stairs(n))
