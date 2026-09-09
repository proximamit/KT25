class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating objects
student1 = Student("Rose", 17)
student2 = Student("Jack Dawson", 21)

student1.display()
print("*" * 20)
Student.display(student1)

student2.display()

# student1 = one object
# student2 = another object
