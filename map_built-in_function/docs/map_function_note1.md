# map() built-in function

- map() function is a built-in function in python  
- it applies a given **function** to every item of an iterable (like a list, tuple, etc.) 
- map() returns a map object and we need to convert it to a list (or another iterable type)
- the result can be consumed only once
- map() is frequently used with lambda functions
- map() is generally used for transforming items in a sequence

### Syntax
```python
    map(function, iterable, ...)
```
- function - A Function to apply to each element of the iterable.  
            This function can be a built-in function, a user-defined function, or a lambda function

- iterable - A sequence (like list, tuple etc.) whose items we want to process  
            Multiple iterables can be provided, in which case the function should accept a corresponding 
            number of arguments

The map() function takes each element from the iterable and passes it as an argument to the specified function
It then collects the return values of the function for each element and returns them as an iterator  

### There are 3 fundamental operations in functional programming
* Mapping
* Reducing
* Filtering

> **Mapping** - Applies a transformation function to an iterable and produces a new iterable of transformed items  

