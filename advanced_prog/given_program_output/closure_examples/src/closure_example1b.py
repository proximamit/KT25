def outer():
    x = []
    def inner(val):
        x.append(val)
        return x
    return inner

f1 = outer()
f2 = outer()

print(f1.__closure__)
print(f2.__closure__)

print(f1(10))   # Line P    Output: [10]
print("\n Closure cell contents:", f1.__closure__[0].cell_contents)
print("\n Freevars: ", f1.__code__.co_freevars)
print(f1(20))   # Line Q    Output: [10, 20]

# Each closure has its own enclosed state
print(f2(30))   # Line R    Output: [30]
print(f1(40))   # Line S    Output: [10, 20, 40]


"""
Even though outer() has already finished running, inner() still remembers the values in the list.

That remembered environment is the closure
"""
