def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(function, iterable)
even_nums = filter(is_even, numbers)
even_nums_list = list(even_nums)

print(even_nums_list)         # Output: [2, 4, 6, 8, 10]
