# Sets in Python

- A **set** in Python is an unordered collection of **unique elements**

---

### Important Properties

- Elements are **unique**
- Unordered (no indexing)
- Mutable (can add/remove items)
- Very fast membership testing using `in`

---

# Common Set Operations

## Union (`|`)

Combines all unique elements from both sets.

```python
A = {1, 2}
B = {2, 3}

A | B
```

Result:

```python
{1, 2, 3}
```

---

## Difference (`-`)

Removes elements of the second set from the first set.

```python
A = {1, 2, 3}
B = {2}

A - B
```

Result:

```python
{1, 3}
```

---
