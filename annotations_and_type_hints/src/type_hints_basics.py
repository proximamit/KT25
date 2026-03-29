# Basic Variable Annotations

# Variable hints
age: int = 21
name: str = "Charlotte"
is_active: bool = True
price: float = 99.99

# print(f"She is {name} and is {age} years old")
# print(__annotations__)
# __annotations__ is just a dictionary


# Function arguments are annotated similarly to variables, 
# The return type is specified using an arrow (->) before the colon for the 
# function body. 
# If a function doesn't return anything explicitly, its return type is None. 

def greet(user: str, age: int) -> str:
    """Greets a user with their name and age."""
    return f"Hello, {user}, you don't look {age} years old"

print(greet(name, age))
print("\nAnnotations: \n", greet.__annotations__, "\n\n")

def subtract_numbers(a: int, b: int) -> int:
    # a: int and b: int are parameter annotations
    # -> int is the return type annotation
    return a - b

magic_number = sum(map(int, str(age)))
#print(magic_number)
#print(subtract_numbers(age, magic_number))

print(f"Surprised to know that you are {age} years old.")
print(f"You look {subtract_numbers(age, magic_number)}")


# Example to demonstrate, Python Does NOT Enforce Type Hints
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))        # Works
print(add("2", "3"))    # Also works (string concatenation!)

def process(data: list[int]) -> dict[str, int]:
    return {"length": len(data)}


class Person:
    name: str
    age: int

print(Person.__annotations__)
