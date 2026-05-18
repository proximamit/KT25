"""
# Trial 1 

# Since next() returns the first yielded value from the generator, 
# the function immediately returns

def two_sum(nums, target):
    seen = {}

    return next(
        ([seen[target - n], i]
         if target - n in seen
         else seen.setdefault(n, i))
        for i, n in enumerate(nums)
        if target - n in seen or n not in seen
    )

# Fail because - 
# The else branch was meant only to update the dictionary, 
# but it also yields a value
"""

'''
# Trial 2

# Fails because setdefault() both mutates state and returns a value

def two_sum(nums, target):
    seen = {}

    return next(
        result
        for i, n in enumerate(nums)
        for result in (
            [[seen[target - n], i]]
            if target - n in seen
            else [None]
        )
        if result is not None or not seen.setdefault(n, i)
    )
'''

def two_sum(nums, target):
    seen = {}

    return next(
        [seen[target - n], i]
        for i, n in enumerate(nums)
        if (
            (target - n in seen)
            or (seen.setdefault(n, i) is not None and False)
        )
    )

if __name__ == "__main__":
    nums = [5, 4, 8, 1]
    target = 12
    print(two_sum(nums, target))  # Output: [1, 2]