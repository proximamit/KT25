# Example to show how instance attributes can
# override or hide class attributes

# Design
# using can_run flag

class Dog:
    def __init__(self, name, can_run=True):
        self.name = name
        self.can_run = can_run

    def run(self):
        if self.can_run:
            print(f"{self.name} is running!")
        else:
            print(f"{self.name} cannot run. It is limping.")

dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Rocky", can_run=False)

dog1.run()
dog2.run()
dog3.run()

"""
 all dogs have the run() method,
 but the behavior differs depending on the object's state.
"""
