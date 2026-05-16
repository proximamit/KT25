def climbStairs(n: int) -> int:
    # Base cases
    if n <= 2:
        return n
    
    # We only need to track the last two results to find the current one
    # first = ways to reach (n-2), second = ways to reach (n-1)
    first, second = 1, 2
    
    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current
        
    return second

if __name__ == "__main__":
    # Testing the examples
    print(f"n = 2: {climbStairs(2)} ways") # Output: 2 ways
    print(f"n = 3: {climbStairs(3)} ways") # Output: 3 ways
    print(f"n = 5: {climbStairs(5)} ways") # Output: 8 ways
    print(f"n = 6: {climbStairs(6)} ways") # Output: 13 ways
    # Example
    print(f"Input: n = 1 | Output: {climbStairs(1)}")

    # Example
    print(f"Input: n = 0 | Output: {climbStairs(0)}")

    # Testing upper constraint limits
    print(f"Input: n = 45 | Output: {climbStairs(45)}")
