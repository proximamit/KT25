# Basic implementation of the
# State Design Pattern

class HealthyState:
    def run(self, dog):
        print(f"{dog.name} is running.")


class InjuredState:
    def run(self, dog):
        print(f"\n\t{dog.name} is limping.\n")

class ExhaustedState:
    def run(self, dog):
        print(f"{dog.name} is too tired to run.")

class SleepingState:
    def run(self, dog):
        print(f"{dog.name} is sleeping.")

class Dog:
    def __init__(self, name):
        self.name = name
        self.state = HealthyState()

    def run(self):
        self.state.run(self)

    def accident(self):
        self.state = InjuredState()

    def training_drill(self):
        self.state = ExhaustedState()

    def take_rest(self):
        self.state = SleepingState()

    def wake_up(self):
        self.state =  HealthyState()

dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Rocky")

dog1.run()
dog2.run()
dog3.run()
print("\nAfter some time...\n")
dog3.accident()

dog1.run()
dog2.run()
dog3.run()

dog2.training_drill()
dog2.run()
dog2.take_rest()
dog2.wake_up()
dog2.run()
