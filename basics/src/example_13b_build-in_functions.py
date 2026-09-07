"""
Python's builtins module contains things that are callable but aren't 
technically functions-

for example:

int
str
list
dict
Exception
object

These are classes/types, not functions, although they are callable.
"""

import builtins
import inspect
import sys

builtin_functions = []

for name in dir(builtins):
    obj = getattr(builtins, name)

    if inspect.isbuiltin(obj) or inspect.isfunction(obj):
        builtin_functions.append(name)

builtin_functions.sort()

print(f"Python version: {sys.version.split()[0]}")
print(f"Number of built-in functions: {len(builtin_functions)}")
print()

for number, name in enumerate(builtin_functions, start=1):
    print(f"{number:2}. {name}")

# Question:
# What is the issue with the above program
# Issue (hint):
# inspect.isbuiltin(obj) or inspect.isfunction(obj)

'''
 The above program actually prints built-in function objects, 
 not the complete set of things documented by Python as built-in functions
'''

# "Built-in" is not equal to "built-in function"

# range, int, str, list, etc. are built-in types, 
# while len, print, abs, etc. are built-in functions.
# _build_class__ and __import__ are special built-in functions 
#  that happen to be exposed in builtins