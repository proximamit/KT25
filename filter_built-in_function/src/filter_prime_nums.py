# Prime numbers are integers greater than 1 that cannot be exactly divided by any whole
# number other than itself and 1

def is_prime(n):
    """ Determine whether a number n is a prime number"""
    if n < 2:
        return False

    # check whether n is divisible by any number between 2 and square root of n 
    # if a number is divisible by a number greater than it's square root,
    # it must also be divisible by a smaller number already checked
    for i in range(2, int(n**0.5)+1):
        # if the number is divisible by any value of i means n is not a prime
        # the modulo operator % returns the remainder
        if n % i == 0:
            return False
    return True

nums = range(1, 20)

primes = list(filter(is_prime, nums))
non_primes = list(filter(lambda x: not is_prime(x), nums))

print("Prime numbers : ", primes)
print("Non-Prime numbers : ", non_primes)