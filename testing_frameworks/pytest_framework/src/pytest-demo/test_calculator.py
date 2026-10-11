from calculator import add, subtract, divide, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(15, 13) == 2

def test_divide():
    assert divide(100, 25) == 4

def test_multiply():
    assert multiply(3, 4) == 12
