import builtins
import sys
import inspect


def is_dunder(name):
    """Return True if name follows the __xxx__ convention."""
    return name.startswith("__") and name.endswith("__") and len(name) > 4


def get_builtin_types():
    """Find all classes/types exposed by the builtins module."""
    types = []

    for name in dir(builtins):
        obj = getattr(builtins, name)

        if inspect.isclass(obj):
            types.append((name, obj))

    return types


def get_magic_methods(cls):
    """Return dunder methods defined by a class."""
    methods = []

    for name in dir(cls):
        if is_dunder(name):
            obj = getattr(cls, name)

            if callable(obj):
                methods.append(name)

    return sorted(methods)


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

print("=" * 70)
print("PYTHON MAGIC METHOD DISCOVERY")
print("=" * 70)
print(f"Python version : {sys.version.split()[0]}")
print(f"Implementation : {sys.implementation.name}")
print("=" * 70)

all_magic_methods = set()
type_data = []

for type_name, cls in get_builtin_types():
    methods = get_magic_methods(cls)

    if methods:
        type_data.append((type_name, cls, methods))
        all_magic_methods.update(methods)


# ---------------------------------------------------------
# Print methods for every built-in type
# ---------------------------------------------------------

for type_name, cls, methods in type_data:

    print()
    print("-" * 70)
    print(f"{type_name}")
    print("-" * 70)

    for number, method in enumerate(methods, start=1):
        print(f"{number:3}. {method}")


# ---------------------------------------------------------
# Print overall unique count
# ---------------------------------------------------------

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"Python version       : {sys.version.split()[0]}")
print(f"Built-in types found : {len(type_data)}")
print(f"Unique magic methods : {len(all_magic_methods)}")
print("=" * 70)

print()
print("ALL UNIQUE MAGIC METHODS")
print("-" * 70)

for number, method in enumerate(sorted(all_magic_methods), start=1):
    print(f"{number:3}. {method}")
