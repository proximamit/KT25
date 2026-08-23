from types import MethodType

class Dog:
    def eat(self):
        return "Eating"

a = Dog()
b = Dog()

def run(self):
    return "running"

a.run = MethodType(run, a)

a.eat()     # works
b.eat()     # works

a.run()   # works
b.run()   # AttributeError
