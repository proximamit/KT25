class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Bob")

print(p1.__dict__)
p1.say_hello = lambda: f"\nHello from {p1.name}!\n"
print(p1.__dict__)
print(p1.say_hello())  # Hello from Alice!


#print(p2.say_hello())  # AttributeError
print(Person.__dict__)
print(p2.__dict__)
