import builtins
import sys
import inspect


def is_dunder(name):
    return name.startswith("__") and name.endswith("__") and len(name) > 4


def get_own_magic_methods(cls):
    """Return only dunder methods defined directly by cls."""
    methods = []

    for name in cls.__dict__:
        if is_dunder(name):
            obj = getattr(cls, name)    # Guess the bug/issue with this line
            # classmethod has a __annotate__ entry that getattr() 
            # can't retrieve normally

            if callable(obj):
                methods.append(name)

    return sorted(methods)


# ---------------------------------------------------------
# Find built-in classes/types
# ---------------------------------------------------------

builtin_types = []

for name in dir(builtins):
    obj = getattr(builtins, name)

    if inspect.isclass(obj):
        builtin_types.append((name, obj))


# ---------------------------------------------------------
# Print results
# ---------------------------------------------------------

print("=" * 70)
print("PYTHON MAGIC METHOD DISCOVERY")
print("=" * 70)
print(f"Python version : {sys.version.split()[0]}")
print(f"Implementation : {sys.implementation.name}")
print("=" * 70)

all_magic_methods = set()

for type_name, cls in builtin_types:

    methods = get_own_magic_methods(cls)

    if not methods:
        continue

    print()
    print("-" * 70)
    print(f"{type_name}  ({len(methods)} methods)")
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
print(f"Python version              : {sys.version.split()[0]}")
print(f"Built-in types inspected    : {len(builtin_types)}")
print(f"Unique magic methods found  : {len(all_magic_methods)}")
print("=" * 70)

print()
print("ALL UNIQUE MAGIC METHODS")
print("-" * 70)

for number, method in enumerate(sorted(all_magic_methods), start=1):
    print(f"{number:3}. {method}")
