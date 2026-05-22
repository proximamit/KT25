# Decorator based rate-limiter

import time

def rate_limiter(interval):
    last_called = 0

    def wrapper(func):

        def inner(*args, **kwargs):
            nonlocal last_called

            current = time.time()

            if current - last_called >= interval:
                last_called = current
                return func(*args, **kwargs)
            else:
                print("Too soon")

        return inner

    return wrapper

@rate_limiter(2)
def hello():
    print("Hello")

hello()
hello()
time.sleep(5)
hello()
