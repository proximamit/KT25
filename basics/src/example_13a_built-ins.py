import builtins

# Get all names defined in the builtins module
builtin_names = dir(builtins)

# Keep only callable objects (functions, types, etc.)
builtin_functions = [
    name for name in builtin_names
    if callable(getattr(builtins, name))
]

# Sort alphabetically
builtin_functions.sort()

print(f"Python version: {__import__('sys').version.split()[0]}")
print(f"Number of built-in functions: {len(builtin_functions)}")
print()

for number, name in enumerate(builtin_functions, start=1):
    print(f"{number:2}. {name}")
