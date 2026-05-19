def factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            yield i

number = int(input("Enter number: "))

for factor in factors(number):
    print(factor)