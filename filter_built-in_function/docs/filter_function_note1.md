# filter() built-in function

- **filter()** is a built-in function
- it allows to process an iterable and extract those items that satisfy a given condition
- it allows to filter items from a sequence (like a list, tuple, etc.) based on a condition provided by a function
- it returns an iterator, which we can convert to a list or another collection
- **filter()** is useful when we want to extract elements that meet a certain condition  

## Syntax
```python
    filter(function, iterable)
```
- **function** - A function that returns True or False for each item in the iterable
- **iterable** - The sequence(list, tuple, etc.) which we want to filter

### There are 3 fundamental operations in functional programming
* Mapping
* Reducing
* Filtering

> **Filtering** - Applies a predicate, of Boolean-valued, function to an iterable and generates a new iterable containing the items that satisfy the Boolean condition