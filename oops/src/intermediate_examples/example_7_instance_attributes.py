# Example to demonstrate how we don't change the class or the method when the accident happens.
# We change the object's state

class Dog:
    def __init__(self, name):
        self.name = name
        self.injured = False

    def run(self):
        if self.injured:
            print(f"\t{self.name} cannot run. It is limping.")
        else:
            print(f"{self.name} is running.")

    def accident(self):
        self.injured = True
        print(f"\n\t{self.name} had an accident!\n")


dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Rocky")

dog1.run()
dog2.run()
dog3.run()

# Accident happens
dog3.accident()

dog1.run()
dog2.run()
dog3.run()
