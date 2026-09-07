import builtins
import sys
import inspect


def is_dunder(name):
    """Return True for names of the form __xxx__."""
    return (
        isinstance(name, str)
        and name.startswith("__")
        and name.endswith("__")
        and len(name) > 4
    )


def get_builtin_types():
    """Find classes/types exposed by the builtins module."""
    types = []

    for name in dir(builtins):
        try:
            obj = getattr(builtins, name)
        except (AttributeError, TypeError):
            continue

        if inspect.isclass(obj):
            types.append((name, obj))

    return types


def get_magic_methods(cls):
    """
    Find magic methods available on a class.

    Uses dir() to discover names but accesses the class dictionary
    safely to avoid problems with special attributes such as
    __annotate__ in newer Python versions.
    """
    methods = []

    for name in dir(cls):
        if not is_dunder(name):
            continue

        try:
            obj = getattr(cls, name)
        except (AttributeError, TypeError):
            continue

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


builtin_types = get_builtin_types()

all_magic_methods = set()


# ---------------------------------------------------------
# Print magic methods for every built-in type
# ---------------------------------------------------------

for type_name, cls in builtin_types:

    methods = get_magic_methods(cls)

    if not methods:
        continue

    print()
    print("-" * 70)
    print(f"{type_name}  ({len(methods)} magic methods)")
    print("-" * 70)

    for number, method in enumerate(methods, start=1):
        print(f"{number:3}. {method}")

    all_magic_methods.update(methods)


# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"Python version       : {sys.version.split()[0]}")
print(f"Built-in types found : {len(builtin_types)}")
print(f"Unique magic methods : {len(all_magic_methods)}")
print("=" * 70)


# ---------------------------------------------------------
# Print unique list
# ---------------------------------------------------------

print()
print("ALL UNIQUE MAGIC METHODS")
print("-" * 70)

for number, method in enumerate(sorted(all_magic_methods), start=1):
    print(f"{number:3}. {method}")
