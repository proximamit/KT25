# filter even numbers in a list

nums = [1, 2, 3, 4, 5, 6, 7]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                                        #  Output: [2, 4, 6] 