import pytest

@pytest.fixture
def connection():
    conn = open_connection()  # Your setup function

    yield conn

    conn.close()
