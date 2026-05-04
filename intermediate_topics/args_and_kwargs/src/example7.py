# Decorator Pattern Example

"""
When writing decorators, we rarely know the signature of the function we are wrapping.
Using *args and **kwargs ensures the decorator is "signature-agnostic."
"""


import functools
import time

def execution_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs) # Forwarding all arguments
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@execution_timer
def complex_data_process(data, threshold=0.5):
    # Imagine heavy logic here
    return len(data) if threshold > 0 else 0

complex_data_process([1, 2, 3], threshold=0.1)
