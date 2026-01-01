def add_greeting(func):
    def wrapper(name):
        return "Hello, " + func(name)
    return wrapper

@add_greeting
def get_name(name):
    return name

print(get_name("Bob"))

# Output:
# Hello, Bob
