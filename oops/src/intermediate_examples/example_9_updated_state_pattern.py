from abc import ABC, abstractmethod


class DogState(ABC):

    @abstractmethod
    def run(self, dog):
        pass

    def accident(self, dog):
        print(f"{dog.name} cannot have an accident in this state.")

    def training_drill(self, dog):
        print(f"{dog.name} cannot train in this state.")

    def take_rest(self, dog):
        print(f"{dog.name} cannot rest in this state.")

    def wake_up(self, dog):
        print(f"{dog.name} is not sleeping.")


class HealthyState(DogState):

    def run(self, dog):
        print(f"{dog.name} is running.")

    def accident(self, dog):
        dog.change_state(InjuredState())


class InjuredState(DogState):

    def run(self, dog):
        print(f"{dog.name} is limping.")

    def take_rest(self, dog):
        dog.change_state(SleepingState())


class ExhaustedState(DogState):

    def run(self, dog):
        print(f"{dog.name} is too tired to run.")

    def take_rest(self, dog):
        dog.change_state(SleepingState())


class SleepingState(DogState):

    def run(self, dog):
        print(f"{dog.name} is sleeping.")

    def wake_up(self, dog):
        dog.change_state(HealthyState())


class Dog:

    def __init__(self, name):
        self.name = name
        self._state = HealthyState()

    @property
    def state(self):
        return self._state

    def change_state(self, state):
        print(
            f"{self.name}: "
            f"{self._state.__class__.__name__} -> "
            f"{state.__class__.__name__}"
        )
        self._state = state

    def run(self):
        self._state.run(self)

    def accident(self):
        self._state.accident(self)

    def training_drill(self):
        self._state.training_drill(self)

    def take_rest(self):
        self._state.take_rest(self)

    def wake_up(self):
        self._state.wake_up(self)

dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Rocky")

dog1.run()
dog2.run()
dog3.run()

dog1.training_drill()
dog3.accident()

dog1.run()
dog3.run()

"""

Enhancement 1: Introduce a common State interface

Enhancement 2: Give Dog a state property

"""
