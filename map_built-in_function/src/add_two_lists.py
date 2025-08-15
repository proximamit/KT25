# Adding two lists

a = [1, 2, 3]
b = [9, 8, 7]

# lambda arguments: expression
# map(function, iterable)
# map can take multiple iterables and pass their items to the function

lists_sum = list(map(lambda x, y: x + y, a, b))
print(lists_sum)