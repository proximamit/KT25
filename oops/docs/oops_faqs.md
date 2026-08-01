# OOPS - Frequently Asked Questions

---
### Query - Shall I write class Dog or class Dog()
- In other words, parentheses after class name is required or not
- Writing class Dog and class Dog() are functionally identical ways to define a 
class that inherits from no other class

- The parentheses are required only when we are explicitly inheriting from one 
or more base classes
- For modern, preferred, and most concise syntax, omit the parentheses for 
simple, standalone classes

---

### Query - Is `__init__` method in python a constructor or not

- Technically, no, the `__init__` method is not a constructor
- it is an initializer
- Python separates the construction of an object from its initialization into
two distinct steps

### How Object Creation Works in Python

When we instantiate a class, Python executes two separate magic methods behind
the scenes:

1. __new__(cls, ...) (The True Constructor):

    - This is the actual constructor method.
    - It is a class method responsible for allocating memory, physically creating
    the blank object instance, and returning that new instance.

1. __init__(self, ...) (The Initializer):

    - This method receives the freshly created instance (passed automatically as
    self).
    - It does not create anything; it simply populates the object with initial
    attributes and configurations

### Query - Is class variable same as class attribute in Python

Yes. In Python, **class variable** and **class attribute** are often used interchangeably, but there's a small distinction in terminology.

- **Class attribute**: Any attribute that belongs to the class itself.
- **Class variable**: A class attribute that stores data shared by all instances.

In practice, most Python programmers use both terms to mean the same thing.