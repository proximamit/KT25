# Function to find all factors of a number
def find_factors(num):
    print("Factors of", num, "are:")

    for i in range(1, num + 1):
        # Checking Factors - If remainder is 0, then i is a factor of num.
        if num % i == 0:
            print(i)

if __name__ == "__main__":
    # Input from user
    number = int(input("Enter a number: "))

    # Function call
    find_factors(number)