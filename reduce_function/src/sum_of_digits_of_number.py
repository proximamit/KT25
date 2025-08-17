# Write a Python program to sum the digits of a given number 
# using reduce 

from functools import reduce

default_number = 123

def sum_digits(number):
    # Convert the number to a string to iterate over its digits
    #      reduce(function,                iterable[, initializer])
    return reduce(lambda x, y: x + int(y), str(number), 0)

# Example usage
try:
    number = int(input("Enter a number: "))
except ValueError as ve:
    exc_type = type(ve).__name__
    print(f"Invalid input!: \n\t {exc_type}: {ve}, \nUsing default number:- {default_number}")
    number = default_number
except Exception as e:
    exc_type = type(e).__name__
    print(f"An unexpected error occurred.\n\t{exc_type}: {e}\nUsing default value")
    number = default_number

if __name__ == "__main__":
    result = sum_digits(number)
    print(f"The sum of the digits of the number {number} is: {result}")
