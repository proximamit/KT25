# reduce() function

- We need to import it before use
- It applies a function ***cumulatively*** to the items of `iterable`, starting from `initializer`

```python
    from functools import reduce
```

## Syntax
```python
    reduce(function, iterable[, initializer])
```

- **function** - A function that takes two arguments
- **iterable** - The sequence(like a list or tuple) to process
- **initializer** (optional) - A starting value. If provided, it's placed before the first item of the iterable

### There are 3 fundamental operations in functional programming
* Mapping
* Reducing
* Filtering

> **Reducing** - Applies a reduction function to an iterable and returns a single cumulative value