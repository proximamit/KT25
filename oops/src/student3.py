class Student:
    school = "ABC School"   # Class variable (class attribute)

    def __init__(self, name):
        self.name = name     # Instance variable (instance attribute)

s1 = Student("Alice")
s2 = Student("Bob")

print(Student.school)  # ABC School
print(s1.school)        # ABC School
print(s2.school)        # ABC School