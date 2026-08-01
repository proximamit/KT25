class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating objects
s1 = Student("Rose", 17)
s2 = Student("Jack Dawson", 21)

s1.display()
s2.display()
