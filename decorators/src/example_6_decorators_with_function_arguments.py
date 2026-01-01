def multiply_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments before multiplication: {args}")
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@multiply_args
def add(a, b):
    return a + b

print(add(2, 3))  # Returns (2 + 3) * 2 = 10
