# The bitwise NOT operator in Python is represented by the tilde symbol ~
# It inverts every bit in the binary representation of a number 
# (changing 0 to 1 and 1 to 0)

## In Python, the bitwise NOT of any integer x is equal to -(x + 1)

a = 5
print(f"Original: {a} (Binary: {bin(a)})")
result_1 = ~a
print(result_1)  # Output: -6
print(bin(result_1))

x = 9
print(f"Original: {x} (Binary: {bin(x)})")  # Original: 9 (Binary: 0b1001)

result = ~x
print(f"Bitwise NOT: {result} (Binary: {bin(result)})") 
# Bitwise NOT: -10 (Binary: -0b1010)

