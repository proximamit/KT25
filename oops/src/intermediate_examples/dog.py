from abc import ABC, abstractmethod


# ============================================================
# State interface
# ============================================================

class DogState(ABC):

    @abstractmethod
    def run(self, dog):
        pass

    def accident(self, dog):
        return f"{dog.name} cannot have an accident right now."

    def training_drill(self, dog):
        return f"{dog.name} cannot train right now."

    def take_rest(self, dog):
        return f"{dog.name} does not need to rest."

    def wake_up(self, dog):
        return f"{dog.name} is not sleeping."


# ============================================================
# Healthy
# ============================================================

class HealthyState(DogState):

    def run(self, dog):
        return f"{dog.name} is running."

    def accident(self, dog):
        dog.change_state(InjuredState())
        return f"{dog.name} is injured."

    def training_drill(self, dog):
        dog.change_state(ExhaustedState())
        return f"{dog.name} is exhausted after training."


# ============================================================
# Exhausted
# ============================================================

class ExhaustedState(DogState):

    def run(self, dog):
        return f"{dog.name} is too tired to run."

    def take_rest(self, dog):
        dog.change_state(SleepingState(self))
        return f"{dog.name} is sleeping."


# ============================================================
# Injured
# ============================================================

class InjuredState(DogState):

    def run(self, dog):
        return f"{dog.name} is injured and is limping."

    def training_drill(self, dog):
        return f"{dog.name} is injured and cannot train."

    def take_rest(self, dog):
        # An injured dog can sleep, but sleeping doesn't heal it.
        dog.change_state(SleepingState(self))
        return f"{dog.name} is resting."

    def accident(self, dog):
        return f"{dog.name} is already injured."


# ============================================================
# Sleeping
# ============================================================

class SleepingState(DogState):

    def __init__(self, previous_state):
        self.previous_state = previous_state

    def run(self, dog):
        return f"{dog.name} is sleeping."

    def wake_up(self, dog):
        if isinstance(self.previous_state, ExhaustedState):
            # Exhaustion is cured by sleep.
            dog.change_state(HealthyState())
        else:
            # Injury survives sleep.
            dog.change_state(self.previous_state)

        return f"{dog.name} woke up."


# ============================================================
# Context
# ============================================================

class Dog:

    def __init__(self, name):
        self.name = name
        self._state = HealthyState()

    @property
    def state(self):
        return self._state

    def change_state(self, state):
        self._state = state

    def run(self):
        return self._state.run(self)

    def accident(self):
        return self._state.accident(self)

    def training_drill(self):
        return self._state.training_drill(self)

    def take_rest(self):
        return self._state.take_rest(self)

    def wake_up(self):
        return self._state.wake_up(self)

if __name__ == "__main__":

    dog1 = Dog("Buddy")
    dog2 = Dog("Max")
    dog3 = Dog("Rocky")

    print(dog1.run())
    print(dog2.run())
    print(dog3.run())
    print("\nAfter some time...\n")
    print(dog3.accident())
    print("\n")
    print(dog1.run())
    print(dog2.run())
    print(dog3.run())
    print("\n")
    print(dog2.training_drill())
    print(dog2.run())
    print(dog2.take_rest())
    print(dog2.wake_up())
    print(dog2.run())

