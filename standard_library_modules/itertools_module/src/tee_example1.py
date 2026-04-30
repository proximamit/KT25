from itertools import tee

it = iter([1,2,3])
a, b = tee(it)

print(list(a))  # [1,2,3]
print(list(b))  # [1,2,3]