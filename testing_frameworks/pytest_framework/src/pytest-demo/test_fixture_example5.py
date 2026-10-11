## 5. Setup and teardown with `yield`

# Sometimes a fixture needs to perform setup before a test and cleanup afterward.

import pytest

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello, pytest!")

    yield file_path

    # Cleanup can go here if needed

def test_file_content(sample_file):
    assert sample_file.read_text() == "Hello, pytest!"

'''
The sequence is:

1. The fixture creates the file.
2. `yield` provides the file path to the test.
3. The test executes.
4. Code after `yield` runs during fixture teardown.

In this example, `tmp_path` is itself a built-in pytest fixture that supplies a temporary directory. 
Pytest manages its cleanup.

'''
