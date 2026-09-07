import builtins
import sys
import inspect


def is_dunder(name):
    """Return True if name has the __xxx__ form."""
    return (
        isinstance(name, str)
        and name.startswith("__")
        and name.endswith("__")
        and len(name) > 4
    )


def get_builtin_types():
    """
    Find classes/types exposed by the builtins module.

    Returns:
        List of (name, class) tuples.
    """
    builtin_types = []

    for name in dir(builtins):
        try:
            obj = vars(builtins)[name]
        except KeyError:
            continue

        if inspect.isclass(obj):
            builtin_types.append((name, obj))

    return builtin_types


def get_own_magic_methods(cls):
    """
    Return magic/dunder names defined directly by cls.

    IMPORTANT:
    We inspect cls.__dict__ directly rather than using getattr().
    This avoids special attribute behavior in Python 3.14+.
    """

    methods = []

    # vars(cls) is effectively cls.__dict__, but makes our
    # intention explicit and avoids getattr().
    class_dictionary = vars(cls)

    for name, obj in class_dictionary.items():

        if not is_dunder(name):
            continue

        # A magic method can be represented by several descriptor
        # types, so use callable() where appropriate.
        #
        # staticmethod/classmethod need special handling because
        # their descriptor object itself may not be callable.
        if (
            callable(obj)
            or isinstance(obj, (staticmethod, classmethod))
        ):
            methods.append(name)

    return sorted(methods)


# ============================================================
# MAIN PROGRAM
# ============================================================

print("=" * 70)
print("PYTHON MAGIC METHOD DISCOVERY")
print("=" * 70)

print(f"Python version : {sys.version.split()[0]}")
print(f"Implementation : {sys.implementation.name}")

print("=" * 70)


# Find all built-in classes/types
builtin_types = get_builtin_types()

# Keep track of every unique magic method
all_magic_methods = set()


# ============================================================
# Display each built-in type
# ============================================================

for type_name, cls in builtin_types:

    methods = get_own_magic_methods(cls)

    if not methods:
        continue

    print()
    print("-" * 70)
    print(f"{type_name}  ({len(methods)} magic methods)")
    print("-" * 70)

    for number, method in enumerate(methods, start=1):
        print(f"{number:3}. {method}")

    all_magic_methods.update(methods)


# ============================================================
# Summary
# ============================================================

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"Python version              : {sys.version.split()[0]}")
print(f"Built-in types discovered   : {len(builtin_types)}")
print(f"Unique magic methods found  : {len(all_magic_methods)}")

print("=" * 70)


# ============================================================
# Unique magic methods
# ============================================================

print()
print("ALL UNIQUE MAGIC METHODS")
print("-" * 70)

for number, method in enumerate(sorted(all_magic_methods), start=1):
    print(f"{number:3}. {method}")
