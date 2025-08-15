def double(x):
    return x * 2

nums = [1, 2, 3]
mapped1 = map(double, nums)

print(list(mapped1))        # Output: [2, 4, 6]
print(list(mapped1))        # Output: []

"""
In the example above:
- The first list(mapped1) consumes the map object and returns the values
- The second list(mapped1) returns an empty list because the map object is already exhausted

To re-use the transformed data multiple times, convert it to a list or tuple once, and store that
"""
mapped2 = list(map(double, nums))
print(mapped2)          # Output: [2, 4, 6]
print(mapped2)          # Output: [2, 4, 6]