import pytest
from calculator import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, 20, 30),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
