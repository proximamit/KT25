from itertools import groupby

data = sorted([('a',1), ('a',2), ('b',3), ('b',4)])

for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
    