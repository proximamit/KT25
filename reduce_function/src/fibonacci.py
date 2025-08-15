# The Fibonacci sequence is a series of numbers where each number is the sum of two 
# preceding numbers. It starts from 0 and 1 

from functools import reduce

# Function to generate the first n numbers in the Fiboacci series 

def fibonacci_series(n):
    # Initial seed: list of tuples with first two Fibonacci numbers
    #     reduce(function                                , iterable [, initializer])
    fib = reduce(lambda acc, _: acc + [acc[-1] + acc[-2]], range(n-2), [0, 1])
    """
     lambda acc, _: acc + [acc[-1] + acc[-2]] 

    Anonymous function that appends the sum of the last two elements of the list acc
    Iterates n-2 times because the first two Fibonacci numbers [0, 1] are already provided 
    as starting point 
    
    acc is the accumulator, which holds the Fibonacci list as it's being built 
    _ is the current item from the iterable range(n-2) 
    """

    # _ (underscore) A throwaway variable
    ''' The underscore _ is a conventional placeholder for a value that is required 
    syntactically but intentionally unused '''

    return fib[:n]

# Input: number of terms
# num_terms = int(input("Enter number of terms: "))
num_terms = 11

# Output the Fibonacci series
print("Fibonacci Series:")
print(fibonacci_series(num_terms))