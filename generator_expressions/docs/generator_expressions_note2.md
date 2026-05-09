# Generator Expressions

- A generator expression is a concise, high-performance and memory-efficient way
 to create a generator object (an iterator) in Python. 
- It looks almost identical to a list comprehension but uses 
**parentheses** `()` instead of ***square brackets*** `[]`

## Key Characteristics

### Advantages
1. **Lazy evaluation**

- Values computed only when needed.
 
- Unlike list comprehensions, which create the entire list in memory 
immediately, generator expressions produce items one at a time, only when we 
ask for them (on-demand).

2. **Memory efficiency**

- No intermediate collections.

- Because they don't store the full sequence, they are ideal for processing 
large datasets or infinite streams.

3. **Single-Use** 
- Once we iterate through a generator (exhaust it), it cannot be reused;  
we must create a new one. 

4. **Short-circuit behavior**

Works beautifully with:

- next
- any
- all
- sum
- max
- min

## Syntax

```python
(expression for item in iterable if condition)
```

1. expression: The value or operation to yield.
1. item: Each element from the source.
1. iterable: The source data (e.g., a list, range, or file).
1. if condition (optional): Filters which items are processed


## Comparison: Generator vs. List Comprehension

| Feature   | Generator Expression                  | List Comprehension       |
| --------- | ------------------------------------- | ------------------------ |
| Syntax    | (x for x in ...)                      | [x for x in ...]         |
| Memory    | Very low (yields items one-by-one)    | High (stores entire list)|
| Speed     | Faster for large data (no allocation) | Faster for small data    |
| Type      | Returns a <generator object>          | Returns a <list> object  |
| Iteration | Exhaustible (only be iterated once)   | Reusable (it's a list)   |
| Evaluation| Lazy (on-demand)                      | Eager (immediate)        |

---

### Note(s)

- Generator expressions are commonly used as arguments for 
"reduction" functions like `sum()`, `max()`, or `any()`

- Exhaustion - Once we iterate through a generator, it's empty. 
If we try to use it again, it yields nothing.
 
- No Indexing: we cannot do gen_exp[5]. We must use next() or a loop

- Late Binding: If our generator uses a variable from the surrounding scope, 
it looks up that variable when the generator is iterated, not when it is created

### Use Generator Expressions when

1. The dataset is huge
1. We only need to iterate once - Passing data to a function like 
`sum()`, `max()`, or `min()`
1. Pipelining - Feeding the output of one operation into another without 
creating intermediate lists.