class Person:
    def __init__(self, name):
        self.name = name 

    def say_hi(self):
        print("Hello, my name is ", self.name)

person_1 = Person("Anthony")
person_1.say_hi()