from typing import Optional
from typing import Union
from typing import Any
from typing import Callable
from typing import List
from typing import TypedDict
from typing import TypeVar

# Default Values + Type Hints
def power(base: int, exponent: int = 2) -> int:
    return base ** exponent


# Type Hints - Specify Optional values 
def get_user(id: int) -> Optional[str]:
    return "User" if id > 0 else None

# Type Hints - Specify Multiple Types 
def add(x: Union[int, float], y: Union[int, float]) -> float:
    return float(x + y)

# In Python 3.10+
def add_modern(x: int | float, y: int | float) -> float:
    return float(x + y)

def stats(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


# Using Type Hint - Any
# List can contain mixed types
my_list: list[Any] = [1, "two", 3.0, {"four": 4}]


# Type Hint Any = "Do whatever you want, I won't check"

def process(data: Any) -> Any:
    return data

# Type Hint - Object

items: list[object] = [1, "hello", 3.14]

# Type Hint object = "You can pass anything, 
# but prove what it is before using it"
def safer_func(x: object) -> None:
    print(x)

# Type Hint object = "I accept any type, but I won’t assume anything about it."
def are_equal(a: object, b: object) -> bool:
    return a == b


# Example of Annotations which are not Type Hints
# These strings are annotations, but they are not type hints.
"""
def greet(name: "user name") -> "greeting message":
    return "Hello " + name

"""

# Value can be an integer or a string
value: Union[int, str] = 10 

# Python 3.10+ syntax
another_value: int | str = 10 


# Python 3.9+ syntax
user_ids: list[int] = [1, 2, 3]
user_info: dict[str, str] = {"name": "Barbie", "email": "barbie@barbenheimer.com"}
coordinate: tuple[int, int] = (10, 20)

# Python 3.10+ syntax
user_name: str | None 

## User-Defined Classes
# 

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Using custom classes as types just like built-in types
def display_user(user_obj: User) -> None:
    print(f"User: {user_obj.name}, Age: {user_obj.age}")

my_user = User("Charlie", 30)
display_user(my_user)


## Classes with Type Hints

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def intro(self) -> str:
        return f"Hi, I'm {self.name}"

# Callable (Functions as Arguments)


def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

def square(x: int) -> int:
    return x * x

print(apply(square, 5))  # 25

# Custom Types with Type Aliases

Scores = List[int]

def average(scores: Scores) -> float:
    return sum(scores) / len(scores)

# Typed Dictionaries


class User(TypedDict):
    name: str
    age: int

def get_user() -> User:
    return {"name": "Alice", "age": 30}

# Advanced 



T = TypeVar('T')

def first_item(items: List[T]) -> T:
    return items[0]

first_item([1, 2, 3])      # int
first_item(["a", "b"])     # str

# Real World Example

def calculate_average(grades: List[int]) -> float:
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

print(calculate_average([80, 90, 100]))

