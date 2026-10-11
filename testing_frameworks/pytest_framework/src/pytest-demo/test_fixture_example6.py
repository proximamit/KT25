## 6. Fixtures can depend on other fixtures

# Fixtures can request other fixtures as parameters. Pytest resolves the dependencies automatically.

import pytest

@pytest.fixture
def username():
    return "alice"

@pytest.fixture
def user(username):
    return {
        "username": username,
        "role": "admin"
    }

def test_user_role(user):
    assert user["username"] == "alice"
    assert user["role"] == "admin"
