import pytest

# @pytest.fixture tells pytest that numbers() is a fixture.
# return [1, 2, 3, 4, 5] provides the test data.
# The numbers parameter in each test tells pytest to inject that fixture.

@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

def test_numbers_length(numbers):
    assert len(numbers) == 5

def test_numbers_sum(numbers):
    assert sum(numbers) == 15