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

    def training_drill(self, dog):
        dog.change_state(ExhaustedState())


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
        # Check who was sleeping previously to determine post-sleep state
        # If the dog was injured, waking up leads to LimpingState.
        # Otherwise (e.g. from exhaustion), waking up leads to HealthyState.
        if isinstance(dog.previous_state, InjuredState):
            dog.change_state(LimpingState())
        else:
            dog.change_state(HealthyState())


class LimpingState(DogState):
    """State for an injured dog that has slept but still limps when trying to run."""

    def run(self, dog):
        print(f"{dog.name} is limping.")

    def accident(self, dog):
        print(f"{dog.name} is already injured/limping.")


class Dog:

    def __init__(self, name):
        self.name = name
        self._state = HealthyState()
        self.previous_state = None  # Track state before sleeping

    @property
    def state(self):
        return self._state

    def change_state(self, state):
        print(
            f"{self.name}: "
            f"{self._state.__class__.__name__} -> "
            f"{state.__class__.__name__}"
        )
        # Keep track of previous state before changing, useful for sleeping logic
        self.previous_state = self._state
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


# --- Demonstration ---
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print("--- Initial State ---")
dog1.run()

print("\n--- Buddy trains, gets exhausted, rests, wakes up, and runs ---")
dog1.training_drill()
dog1.run()         # Too tired to run
dog1.take_rest()
dog1.wake_up()
dog1.run()         # Back to healthy, can run normally!

print("\n--- Max gets injured, rests, wakes up, and tries to run ---")
dog2.accident()
dog2.run()         # Limping
dog2.take_rest()
dog2.wake_up()
dog2.run()         # Still limping after sleep!
