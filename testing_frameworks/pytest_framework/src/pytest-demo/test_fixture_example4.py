#4. Question: How many times will the following fixture run when both tests execute?

import pytest

@pytest.fixture
def counter():
    print("Fixture executed")
    return 10

def test_one(counter):
    assert counter == 10

def test_two(counter):
    assert counter == 10

## Answer: Once per test
# The fixture runs twice, once for each test, because the default fixture scope is function.
