from itertools import count

for i in count(5, 2):
    if i > 15:
        break
    print(i)
    