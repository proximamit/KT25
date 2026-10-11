import pytest

@pytest.fixture(scope="module")
def shared_data():
    print("\nSetting up shared data")
    return {"status": "ready"}

def test_first(shared_data):
    assert shared_data["status"] == "ready"

def test_second(shared_data):
    assert shared_data["status"] == "ready"
