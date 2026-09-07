import builtins
import sys
import inspect


# ============================================================
# Configuration
# ============================================================

# Exception classes are built-in classes, but normally aren't
# what we mean when studying Python's data model.
EXCLUDE_EXCEPTIONS = True


# ============================================================
# Helper functions
# ============================================================

def is_dunder(name):
    """Return True for names of the form __xxx__."""
    return (
        isinstance(name, str)
        and name.startswith("__")
        and name.endswith("__")
        and len(name) > 4
    )


def is_exception_class(cls):
    """Return True if cls is an exception class."""
    try:
        return issubclass(cls, BaseException)
    except TypeError:
        return False


def get_builtin_types():
    """
    Discover classes exposed by the builtins module.

    Returns:
        List of (name, class) tuples.
    """

    builtin_types = []

    for name, obj in vars(builtins).items():

        if not isinstance(name, str):
            continue

        if not inspect.isclass(obj):
            continue

        if EXCLUDE_EXCEPTIONS and is_exception_class(obj):
            continue

        builtin_types.append((name, obj))

    return sorted(builtin_types, key=lambda item: item[0])


def get_defined_dunders(cls):
    """
    Get dunder names defined directly in cls.__dict__.

    This does NOT include inherited methods.
    """

    return sorted(
        name
        for name in vars(cls)
        if is_dunder(name)
    )


def get_all_dunders(cls):
    """
    Get all dunder names visible on cls, including inherited names.

    Uses dir() only to discover names. We don't call getattr().
    """

    return sorted(
        name
        for name in dir(cls)
        if is_dunder(name)
    )


def get_inherited_dunders(cls):
    """
    Get dunder names available on cls but not defined directly
    by cls.
    """

    defined = set(get_defined_dunders(cls))
    available = set(get_all_dunders(cls))

    return sorted(available - defined)


def get_defining_class(cls, method_name):
    """
    Find the first class in the MRO that defines method_name.

    Returns:
        The class that defines the name, or None.
    """

    for base in cls.__mro__:
        if method_name in vars(base):
            return base

    return None


# ============================================================
# Header
# ============================================================

print()
print("=" * 78)
print("PYTHON DATA MODEL EXPLORER")
print("=" * 78)

print(f"Python version : {sys.version.split()[0]}")
print(f"Implementation : {sys.implementation.name}")

print("=" * 78)


# ============================================================
# Discover built-in types
# ============================================================

builtin_types = get_builtin_types()

all_magic_methods = set()


# ============================================================
# Display each type
# ============================================================

for type_name, cls in builtin_types:

    defined = get_defined_dunders(cls)
    inherited = get_inherited_dunders(cls)
    available = get_all_dunders(cls)

    # Ignore classes that have no dunders at all.
    if not available:
        continue

    all_magic_methods.update(available)

    print()
    print()
    print("#" * 78)
    print(f"# {type_name}")
    print("#" * 78)

    print()
    print(f"Type                  : {type_name}")
    print(f"Defined here          : {len(defined)}")
    print(f"Inherited              : {len(inherited)}")
    print(f"Total available       : {len(available)}")

    # --------------------------------------------------------
    # Defined directly by this class
    # --------------------------------------------------------

    print()
    print("  DEFINED HERE")
    print("  " + "-" * 68)

    if defined:
        for number, name in enumerate(defined, start=1):
            print(f"  {number:3}. {name}")
    else:
        print("       (none)")

    # --------------------------------------------------------
    # Inherited from another class
    # --------------------------------------------------------

    print()
    print("  INHERITED")
    print("  " + "-" * 68)

    if inherited:
        for number, name in enumerate(inherited, start=1):

            defining_class = get_defining_class(cls, name)

            if defining_class is not None:
                defining_name = defining_class.__name__
            else:
                defining_name = "unknown"

            print(
                f"  {number:3}. {name:<30}"
                f" ← {defining_name}"
            )
    else:
        print("       (none)")


# ============================================================
# Global summary
# ============================================================

print()
print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)

print(f"Python version              : {sys.version.split()[0]}")
print(f"Implementation              : {sys.implementation.name}")
print(f"Built-in types discovered   : {len(builtin_types)}")
print(f"Unique magic methods        : {len(all_magic_methods)}")

print("=" * 78)


# ============================================================
# Global unique list
# ============================================================

print()
print("ALL UNIQUE MAGIC METHODS")
print("-" * 78)

for number, name in enumerate(sorted(all_magic_methods), start=1):
    print(f"{number:3}. {name}")


print()
print("=" * 78)
print("END")
print("=" * 78)
