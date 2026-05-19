import math

# Factors always come in pairs
# Once we pass the square root, we find the same pairs in reverse order
# Hence checking till square root of a given number

def factors(num):
    result = set()

    for i in range(1, int(math.sqrt(num)) + 1):
        # check if the number divides evenly (no remainder)
        if num % i == 0:
            result.add(i)           # Add the small factor
            result.add(num // i)    # Add the partner factor

    return sorted(result)

if __name__ == "__main__":
    number = int(input("Enter number: "))
    print(factors(number))


"""
// operator is known as the Floor Division operator

"""

'''
 the modulo operator (%), returns the remainder of the division
'''