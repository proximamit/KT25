import pytest

@pytest.fixture
def user():
    return {
        "name": "Alice",
        "age": 25,
        "active": True
    }

def test_user_name(user):
    assert user["name"] == "Alice"

def test_user_is_active(user):
    assert user["active"] is True
