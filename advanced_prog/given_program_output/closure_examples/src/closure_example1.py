def outer():
    x = []
    def inner(val):
        x.append(val)
        return x
    return inner

f1 = outer()
f2 = outer()

print(f1(10))   # Line P    Output: [10]
print(f1(20))   # Line Q    Output: [10, 20]
print(f2(30))   # Line R    Output: [30]
print(f1(40))   # Line S    Output: [10, 20, 40]
