# Sliding window

from itertools import islice

def window(iterable, size):
    it = iter(iterable)
    result = tuple(islice(it, size))
    if len(result) == size:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

print(list(window([1,2,3,4,5], 3)))