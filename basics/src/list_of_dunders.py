import builtins
import sys

# Find all dunder names in the builtins module
dunders = [
    name
    for name in dir(builtins)
    if name.startswith("__") and name.endswith("__")
]

dunders.sort()

print("=" * 50)
print(f"Python version : {sys.version.split()[0]}")
print(f"Dunder count   : {len(dunders)}")
print("=" * 50)
print()

for number, name in enumerate(dunders, start=1):
    print(f"{number:3}. {name}")

"""
There are actually multiple things 
with double underscores before and after:


Dunder names in builtins - __name__, __doc__, __import__, __build_class__, etc.
Python's magic/dunder methods - __init__, __str__, __add__, __getitem__, etc.

and

Built-in functions - print, len, open, __import__, etc.

"""