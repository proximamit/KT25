# Intentional Mutable Default arg example

def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]

    if n < 2:
        return n

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

 # First execution (calculates and fills the cache)
print(fibonacci(5))  # Output: 5

# Let's inspect the hidden cache after the first run
print(fibonacci.__defaults__)  
# Output: ({2: 1, 3: 2, 4: 3, 5: 5},) <-- The data is trapped here!

# Second execution with a different number
print(fibonacci(6))  # Output: 8
