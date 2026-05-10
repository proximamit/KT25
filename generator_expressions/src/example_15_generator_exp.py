# Program to search for the first pair of numbers 
# (one from list a and one from list b) that add up to exactly 8.

# Cartesian-product search

a = [1, 2, 3]
b = [4, 5, 6]

pair = next(
    (
        (x, y)
        for x in a
        for y in b
        if x + y == 8
    ),
    None
)

print(pair)
