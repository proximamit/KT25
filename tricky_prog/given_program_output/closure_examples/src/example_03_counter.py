def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()

print(c())  # Output: 1
print(c())  # Output: 2
print(c())  # Output: 3

# The variable count persists across calls

"""
Using nonlocal tells Python to use the variable from the enclosing scope.
"""
