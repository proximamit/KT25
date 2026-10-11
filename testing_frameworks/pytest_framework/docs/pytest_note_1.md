### Pytest

- **pytest** is a popular Python testing framework that helps to check whether our code works as expected
- It's beginner-friendly
- Requires very little setup, and 
- It is widely used in real-world Python projects

###  Verify Python is installed

`python3 --version`

### Install pytest using pip

`python3 -m pip install pytest`

###  Verify Pytest is installed

`python3 -m pytest --version`

### Syntax

- `test_` — pytest uses this naming convention to discover test functions.
- `assert` — checks whether an expression is true.

### Run the tests

- `python3 -m pytest`

### Show each test name and result

- `python3 -m pytest -v`

### Run a specific test file

- `python3 -m pytest -v test_calculator.py`

### Run tests whose names match add

- `python3 -m pytest -v -k add`

### Stop after the first failure

- `python3 -m pytest -x`

### List tests without running them

- `python3 -m pytest --collect-only`

### Test multiple inputs with parametrization

- Instead of writing separate functions for every input, use `@pytest.mark.parametrize`.

### Use fixtures for reusable setup

