# Flatten list of lists

from itertools import chain

matrix = [[1,2],[3,4],[5]]
flat = list(chain.from_iterable(matrix))
print(matrix)
print("\n")
print(flat)
