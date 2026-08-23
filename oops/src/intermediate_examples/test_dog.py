import pytest

from dog import Dog


# ============================================================
# Initial state
# ============================================================

def test_dog_starts_healthy():
    dog = Dog("Buddy")

    assert dog.state.__class__.__name__ == "HealthyState"
    assert dog.run() == "Buddy is running."


# ============================================================
# Healthy -> Exhausted
# ============================================================

def test_training_makes_healthy_dog_exhausted():
    dog = Dog("Buddy")

    result = dog.training_drill()

    assert result == "Buddy is exhausted after training."
    assert dog.state.__class__.__name__ == "ExhaustedState"


def test_exhausted_dog_cannot_run():
    dog = Dog("Buddy")

    dog.training_drill()

    assert dog.run() == "Buddy is too tired to run."


# ============================================================
# Exhausted -> Sleeping -> Healthy
# ============================================================

def test_exhausted_dog_can_rest():
    dog = Dog("Buddy")

    dog.training_drill()

    result = dog.take_rest()

    assert result == "Buddy is sleeping."
    assert dog.state.__class__.__name__ == "SleepingState"


def test_sleeping_exhausted_dog_becomes_healthy_after_waking():
    dog = Dog("Buddy")

    dog.training_drill()
    dog.take_rest()
    dog.wake_up()

    assert dog.state.__class__.__name__ == "HealthyState"
    assert dog.run() == "Buddy is running."


# ============================================================
# Healthy -> Injured
# ============================================================

def test_accident_makes_healthy_dog_injured():
    dog = Dog("Buddy")

    result = dog.accident()

    assert result == "Buddy is injured."
    assert dog.state.__class__.__name__ == "InjuredState"


def test_injured_dog_limps_instead_of_running():
    dog = Dog("Buddy")

    dog.accident()

    assert dog.run() == "Buddy is injured and is limping."


# ============================================================
# Injured -> Sleeping -> Injured
# ============================================================

def test_injured_dog_can_rest():
    dog = Dog("Buddy")

    dog.accident()

    result = dog.take_rest()

    assert result == "Buddy is resting."
    assert dog.state.__class__.__name__ == "SleepingState"


def test_sleep_does_not_heal_injured_dog():
    dog = Dog("Buddy")

    dog.accident()
    dog.take_rest()
    dog.wake_up()

    assert dog.state.__class__.__name__ == "InjuredState"


def test_injured_dog_still_limps_after_sleep():
    dog = Dog("Buddy")

    dog.accident()
    dog.take_rest()
    dog.wake_up()

    assert dog.run() == "Buddy is injured and is limping."


# ============================================================
# Injured dog cannot train
# ============================================================

def test_injured_dog_cannot_train():
    dog = Dog("Buddy")

    dog.accident()

    result = dog.training_drill()

    assert result == "Buddy is injured and cannot train."
    assert dog.state.__class__.__name__ == "InjuredState"


# ============================================================
# Multiple dogs are independent
# ============================================================

def test_multiple_dogs_have_independent_states():
    buddy = Dog("Buddy")
    max_dog = Dog("Max")
    rocky = Dog("Rocky")

    buddy.training_drill()
    max_dog.accident()

    assert buddy.run() == "Buddy is too tired to run."
    assert max_dog.run() == "Max is injured and is limping."
    assert rocky.run() == "Rocky is running."
