# Infinite generators + generator expressions

# use a generator to create an infinite sequence of even numbers, 
# but only print the first five

# Demonstrates laziness beautifully.

from itertools import count

evens = (
    n
    for n in count(0)
    if n % 2 == 0
)

for _ in range(5):
    print(next(evens))
