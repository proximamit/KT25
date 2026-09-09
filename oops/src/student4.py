# self = the current object that is using/calling the method

class Student:
    def introduce(self):
        print("I am a student")

# create an object
student1 = Student()

student1.introduce()

"""
When we write:

student1.introduce()

Python automatically passes student1 to the self parameter
"""
# Internally, it translates to
Student.introduce(student1)

# inside introduce(), self refers to student1
