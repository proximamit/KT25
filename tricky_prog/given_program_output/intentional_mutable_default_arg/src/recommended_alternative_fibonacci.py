# calculates the nth Fibonacci number using recursion 
# using a specialized optimization called memoization 
# to make it run much faster

# Using decorators

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n

    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

# Execution - calculate the 10th Fibonacci number
print(fibonacci_lru(10))  # Output: 55

# We can check the cache hits and misses directly
print(fibonacci_lru.cache_info())  
# Output: CacheInfo(hits=8, misses=11, maxsize=None, currsize=11)

# We can clear the cache at any time safely
fibonacci_lru.cache_clear()
