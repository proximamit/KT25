import builtins
import sys
import inspect
from collections import defaultdict


# ============================================================
# CONFIGURATION
# ============================================================

# True  -> include exception classes such as ValueError
# False -> exclude them from the data-model reference
INCLUDE_EXCEPTIONS = False

# True -> show inherited magic methods as well as directly
#         defined magic methods
SHOW_INHERITED = True


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def is_dunder(name):
    """
    Return True if name follows the Python dunder convention:

        __something__
    """

    return (
        isinstance(name, str)
        and name.startswith("__")
        and name.endswith("__")
        and len(name) > 4
    )


def is_exception_class(cls):
    """Return True if cls is derived from BaseException."""

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

    result = []

    for name, obj in vars(builtins).items():

        if not isinstance(name, str):
            continue

        if not inspect.isclass(obj):
            continue

        if not INCLUDE_EXCEPTIONS and is_exception_class(obj):
            continue

        result.append((name, obj))

    return sorted(result, key=lambda item: item[0].lower())


def get_defined_dunders(cls):
    """
    Return dunder names defined directly in cls.__dict__.

    Inherited attributes are NOT included.
    """

    return {
        name
        for name in vars(cls)
        if is_dunder(name)
    }


def get_available_dunders(cls):
    """
    Return all dunder names visible through the class.

    This includes inherited dunders.
    """

    return {
        name
        for name in dir(cls)
        if is_dunder(name)
    }


def get_defining_class(cls, name):
    """
    Find the first class in the MRO that defines 'name'.

    Returns:
        The defining class, or None.
    """

    for base in cls.__mro__:

        if name in vars(base):
            return base

    return None


def format_mro(cls):
    """
    Return a readable MRO string.
    """

    names = [base.__name__ for base in cls.__mro__]

    return " → ".join(names)


# ============================================================
# DISCOVER BUILT-IN TYPES
# ============================================================

builtin_types = get_builtin_types()


# ============================================================
# BUILD MAGIC-METHOD DATABASE
# ============================================================

# Structure:

# {
#     "__add__": [
#         (type_name, "defined"),
#         (type_name, "inherited", defining_class),
#         ...
#     ]
# }

magic_methods = defaultdict(list)


for type_name, cls in builtin_types:

    defined = get_defined_dunders(cls)
    available = get_available_dunders(cls)

    for method_name in available:

        # ----------------------------------------------------
        # Method defined directly by this type
        # ----------------------------------------------------

        if method_name in defined:

            magic_methods[method_name].append(
                (
                    type_name,
                    "defined",
                    cls.__name__
                )
            )

        # ----------------------------------------------------
        # Method inherited from a parent
        # ----------------------------------------------------

        elif SHOW_INHERITED:

            defining_class = get_defining_class(
                cls,
                method_name
            )

            if defining_class is not None:

                magic_methods[method_name].append(
                    (
                        type_name,
                        "inherited",
                        defining_class.__name__
                    )
                )


# ============================================================
# HEADER
# ============================================================

print()
print("=" * 80)
print("PYTHON MAGIC-METHOD REFERENCE")
print("=" * 80)

print(f"Python version       : {sys.version.split()[0]}")
print(f"Implementation       : {sys.implementation.name}")
print(f"Built-in types       : {len(builtin_types)}")
print(f"Unique magic methods : {len(magic_methods)}")

print("=" * 80)


# ============================================================
# MAGIC METHODS
# ============================================================

for method_name in sorted(magic_methods):

    entries = magic_methods[method_name]

    print()
    print()
    print("#" * 80)
    print(f"# {method_name}")
    print("#" * 80)

    defined = [
        entry
        for entry in entries
        if entry[1] == "defined"
    ]

    inherited = [
        entry
        for entry in entries
        if entry[1] == "inherited"
    ]

    # --------------------------------------------------------
    # Directly defined
    # --------------------------------------------------------

    print()
    print("  DEFINED BY")
    print("  " + "-" * 72)

    if defined:

        for type_name, _, defining_class in sorted(defined):
            print(
                f"      {type_name:<25}"
                f" ({defining_class})"
            )

    else:
        print("      (none)")


    # --------------------------------------------------------
    # Inherited
    # --------------------------------------------------------

    if SHOW_INHERITED:

        print()
        print("  INHERITED BY")
        print("  " + "-" * 72)

        if inherited:

            for type_name, _, defining_class in sorted(inherited):

                print(
                    f"      {type_name:<25}"
                    f" ← {defining_class}"
                )

        else:
            print("      (none)")


# ============================================================
# COMPACT REFERENCE
# ============================================================

print()
print()
print("=" * 80)
print("COMPACT MAGIC-METHOD REFERENCE")
print("=" * 80)

print()
print(
    f"{'MAGIC METHOD':<25}"
    f"{'DEFINED BY':<35}"
)

print("-" * 80)


for method_name in sorted(magic_methods):

    entries = magic_methods[method_name]

    defined = sorted(
        entry[0]
        for entry in entries
        if entry[1] == "defined"
    )

    if defined:

        types = ", ".join(defined)

        print(
            f"{method_name:<25}"
            f"{types:<35}"
        )


# ============================================================
# SUMMARY
# ============================================================

print()
print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)

print(f"Python version       : {sys.version.split()[0]}")
print(f"Implementation       : {sys.implementation.name}")
print(f"Built-in types       : {len(builtin_types)}")
print(f"Magic methods        : {len(magic_methods)}")

defined_count = sum(
    1
    for method in magic_methods.values()
    if any(entry[1] == "defined" for entry in method)
)

print(f"Methods defined      : {defined_count}")

if SHOW_INHERITED:

    inherited_count = sum(
        1
        for method in magic_methods.values()
        if any(entry[1] == "inherited" for entry in method)
    )

    print(f"Methods inherited    : {inherited_count}")

print("=" * 80)


# ============================================================
# OPTIONAL: SHOW TYPE MRO
# ============================================================

print()
print()
print("=" * 80)
print("BUILT-IN TYPE MRO")
print("=" * 80)

for type_name, cls in builtin_types:

    print()
    print(f"{type_name:<25}: {format_mro(cls)}")

print()
print("=" * 80)
print("END OF REFERENCE")
print("=" * 80)
