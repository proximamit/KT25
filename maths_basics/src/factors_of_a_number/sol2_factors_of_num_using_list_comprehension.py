def find_factors(num):
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(find_factors(number))