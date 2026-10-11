import os

#  example, using `monkeypatch` to test environment variables:

def test_environment_variable(monkeypatch):
    monkeypatch.setenv("APP_ENV", "testing")

    assert os.getenv("APP_ENV") == "testing"

# Pytest restores the environment variable to its previous state after the test.
