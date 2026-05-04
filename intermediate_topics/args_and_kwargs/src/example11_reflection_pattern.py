# Dynamic Function Calls (Reflection Pattern)

def greet(name, age):
    return f"{name} is {age} years old"

data = {"name": "Alice", "age": 25}

print(greet(**data))
