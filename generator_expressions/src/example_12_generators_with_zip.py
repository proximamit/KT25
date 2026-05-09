a = [1, 2, 3]
b = [4, 5, 6]

dot_product = sum(
    x * y
    for x, y in zip(a, b)
)

print(dot_product)
