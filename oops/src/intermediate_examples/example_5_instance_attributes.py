#  remove/hide the method specifically for one instance

# dog3.run = dog3.limp
# Override behavior for one object

class Dog:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} is running!")

    def limp(self):
        print(f"\t{self.name} is limping.")

dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Rocky")

dog1.run()
dog2.run()
dog3.run()
print("\n")
#print(dog3.__dict__)

# override run for dog3
dog3.run = dog3.limp

dog1.run()
dog2.run()
dog3.run()
#print(dog3.__dict__)
#print(dog1.__dict__)

"""
This example demonstrates
how an instance attribute can override a class method for only one object
"""
