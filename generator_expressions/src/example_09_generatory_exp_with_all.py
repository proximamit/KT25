#nums = [2, 4, 6, 8]
nums = [2, 4, 5, 6, 8]

all_even = all(
    n % 2 == 0
    for n in nums
)

print(all_even)

# Stops at first failure

# all(cond(x) for x in items)
