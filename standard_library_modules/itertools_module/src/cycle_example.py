from itertools import cycle

colors = cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors))
    