import pytest
from calculator import divide

# This test passes when the function raises `ZeroDivisionError`.
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
