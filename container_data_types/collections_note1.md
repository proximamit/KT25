<a name="top"></a>

# Collections (Container data types) 

- **Container data types** also known as ***Collections*** in Python are used to store and organize multiple items (data)
- **Collections** are data structures that **hold or contain other objects** [^1](#footnote-1)
- **Container data types** are fundamental to writing effective, clean, and efficient Python code
- These can be broadly categorized into ***built-in collections*** and specialized collections provided by the ***collections module*** from Python's standard library

---
### Mutable and Immutable

- ***mutable*** - Something that **CAN be changed** after it's created
- ***immutable*** - Something that **CANNOT be changed** once created

---
## Built-in Collections

- There are **four** main **built-in container types**
- These are general purpose built-in containers

| Type                              | Description                                   |
| ----------------------------------| --------------------------------------------- |
| `list`                            | Ordered, mutable sequence of items            |
| `tuple`                           | Ordered, immutable sequence of items          |
| `set`                             | Unordered, mutable collection of unique items |
| `dict` **Before Python 3.7**      | Unordered collection of key-value pairs       |
| `dict` **Python 3.7 and later**   | Ordered collection of key-value pairs         |

---
### Lists

A `list` is like an array - it keeps the order of elements and can be modified

* **Ordered** and ***mutable*** sequences of elements
* Can store **heterogeneous** data types
* Allow **duplicate** elements
* Elements are accessed by integer indices
* Defined using **square brackets []**
* Example: my_list = [1, 'hello', 3.14]

> `list()` constructor can be used to convert other iterables (like tuples, strings) into a list

---

### Tuples

A `tuple` is like a list but **cannot be changed** after creation. i.e. no adding, removing or modifying elements

* **Ordered** and ***immutable*** sequences of elements
* Can store **heterogeneous** (Mixed) data types
* Allow **duplicate** elements
* Elements are accessed by integer indices  (**Indexable**)
* Defined using **parentheses ()**
* Example: my_tuple = (1, 'hello', 3.14)

> `tuple()` constructor can be used to convert other iterables to a tuple

---

### Dictionaries

* Collections of ***key-value pairs***
    - Unordered - Before Python 3.7
    - Ordered - Python 3.7 and later
* **Mutable**
* Keys must be ***unique*** and **immutable**, values can be of any type
* Elements are accessed by their associated keys
* Defined using **curly braces {}** with the ***key-value pairs*** separated by **colons**
* Example: my_dict = {"name": "Alice", "age": 30}

> `dict()` constructor can be used to create a dictionary object in Python

> Keys in dictionaries must be unique and hashable.
[^2](#footnote-2)

---

### Sets

* **Unordered** collections of **unique**, ***hashable*** elements
* Mutable
* ***Do not allow duplicate*** elements
* Defined using **curly braces {}** or the **set()** constructor
* Example: my_set = {1, 2, 3}

---
---

## collections module in Python's standard library 
- `collections` module is a Built-in module
- Provides specialized collections
- The `collections` module provides enhanced versions of built-in types and new specialized containers for specific use cases

| `collections` module Class        | Description                               |
| ----------------------------------|-------------------------------------------|
| Counter                           | Frequency Counter                         |
| namedtuple                        | Tuple with named fields                   |
| deque                             | Double-ended queue                        |
| ChainMap                          | Combines multiple dictionaries            |
| OrderedDict                       | Dictionary maintaining insertion order    |
| defaultdict                       | Dict with default values for missing keys |


### Notes:

<a name="footnote-1">[^1]</a> a container or a collection is a single variable that can store many values
<a name="footnote-2">[^2]</a>
Hashable objects are crucial for efficient storage and retrieval
Hashable objects are **immutable** - their value cannot be changed after creation.
Dictionaries use hashing to quickly locate values assiciated with their keys
Similarly, only hashable objects can be elements of sets

Examples of hashable and unhashable objects
* Hashable - Integers, floats, strings, tuples(if all their elements are also hashable)
* Unhashable - Lists, dictionaries, sets (as they are mutable)
(#top)
