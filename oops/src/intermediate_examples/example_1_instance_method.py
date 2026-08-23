## Example: Where a method belongs to an object but not to a class

from types import MethodType

class Giraffe:
    def __init__(self, name):
        self.name = name

giraffe1 = Giraffe("Giru")
giraffe2 = Giraffe("Raffe")

def hum(self):
    return f"{self.name} says Hummmm!"

giraffe1.hum = MethodType(hum, giraffe1)

print(giraffe1.hum())   # Giru says Hummmm!

print(giraffe2.hum())   # AttributeError
# AttributeError: 'Giraffe' object has no attribute 'hum'


"""
A class method is defined on the class and normally available to its instances.

An instance method can be attached to one particular object
without being added to the class.
"""
