# Dictionaries in Python

- Dictionary is a built-in data structure in Python
- Values in a dictionary can be of **any type** and **duplicate** values are allowed

### Python Dictionary Methods

- `get()` - To get the value of the specified key
    - If the key is not found, the default value is returned
    - Using square brackets, trying to access values of a key that doesn't exist raises `KeyError`. 
    - To avoid that, `.get()` method can be used

- `items()` - Returns a list containing a tuple for each key value pair

- `keys()` - Returns a list containing the dictionary's keys

- `values()` - Returns a list of all the values in the dictionary

- `clear()` - Removes all items from the dictionary

- `update()` - Updates the dictionary with the specified key-value pair

- `pop()` - Removes a key and returns it value

- `popitem()`- Removes and returns last item

- `copy()` - Returns a shallow copy

- `fromkeys()` - Creates dict from iterable

- `setdefault()` - Gets value or sets key with default