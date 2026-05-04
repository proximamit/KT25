# Wrapper Functions / Decorators

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@logging_decorator
def multiply(a, b):
    return a * b

print(multiply(3, 4))