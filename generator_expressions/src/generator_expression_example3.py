# Example to Convert Generator to List

gen = (x * x for x in range(11))
result = list(gen)
print(result)

# Example of Generator with condition
even_squares = (x**2 for x in range(11) if x % 2 == 0)

for num in even_squares:
    print(num, end="\t")

# Example - Summing Elements from Generator
total = sum(x for x in range(11))
print(f"\n\nSum of first 10 numbers:- ", total)

# Example of using `next()` With Generator
gen = (x * x for x in range(5))

print(next(gen))  # 0
print(next(gen))  # 1

# Example of Nested Generator Expression
gen = ((x, y) for x in range(3) for y in range(2))
print(list(gen))

# Log File Processing (Large File)
"""
# This avoids reading the entire file into memory

with open("log_file.txt") as file:
    error_lines = (line for line in file if "ERROR" in line)
    for line in error_lines:
        print(line.strip())

"""
# Example to show - We can't index a generator
gen = (x for x in range(10))
#print(gen[0])
# Output: TypeError: 'generator' object is not subscriptable
