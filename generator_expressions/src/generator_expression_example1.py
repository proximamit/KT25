# Create a generator expression to yield squares of numbers

#             (expression for item in iterable if condition)
squares_generator = (x**2 for x in range(1, 11))

# Iterate and print values
for square in squares_generator:
    print(square, end="\t")