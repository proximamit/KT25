# OOPS

- Object-Oriented Programming (OOP) means modeling a program using objects that represent real things.
- In object-oriented programming we write classes that represent real-world 
things and situations
- When we write a class, we define the general behavior that a whole category of objects can have.
- Making an object from a class is called **instantiation**, and we work with instances of a class
- A function that's part of a class is known as a **method**
---

## The __init__() method

- The __init__() method is called automatically when an object is created. 
- It initializes the object's data.

The __init__() method
- has two leading underscores and two trailing underscores
- is a special method which runs automatically whenever we create a new instance based on the class



---

## The self parameter

- is required in the method definition,
- self refers to the current object.
- It is used to access the object's attributes and methods.
- It must be the first parameter of instance methods (i.e. it must come before 
the other parameters).

---

## Advantages of Classes and Objects

- Organize code into reusable components.
- Improve readability and maintainability.
- Support code reuse through inheritance.
- Make programs easier to model using real-world entities.

# Summary

| Concept     | Description                     | Example          |
| ----------- | ------------------------------- | ---------------- |
| Class       | Blueprint for creating objects  | `class Student:` |
| Object      | Instance of a class             | `s1 = Student()` |
| Attribute   | Data stored in an object        | `self.name`      |
| Method      | Function defined inside a class | `display()`      |
| Constructor | Initializes object data         | `__init__()`     |
| `self`      | Refers to the current object    | `self.name`      |
