# Many Python functions return multiple values
# Useful when we only need part of the result

def get_user():
    return "Alice", 25, "Wonderland"

name, _, _ = get_user()
print(name)  # Alice
