"""
def log_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        return func(self, *args, **kwargs)
    return wrapper

class Person:
    def __init__(self, name):
        self.name = name

    @log_method
    def greet(self):
        print(f"Hello, {self.name}")

p = Person("Alice")
p.greet()  # The method is decorated

# Output:
# Calling greet with arguments () and {}
# Hello, Alice

"""

def log_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        return func(self, *args, **kwargs)
    return wrapper

class Person:
    def __init__(self, name):
        self.name = name

    @log_method
    def greet(self, mood, greeting="Hello"):
        print(f"{greeting}, {self.name}. \n{mood} New Year!")

p = Person("Alice")
# Calling greet with extra positional and keyword arguments
p.greet("Happy", greeting="Good morning")  # Pass positional and keyword arguments
#"""

# Output:
# Calling greet with arguments ('Happy',) and {'greeting': 'Good morning'}
# Good morning, Alice. 
# Happy New Year!
