# Generator Expressions

- ***Generator expressions*** in Python are a concise way to create ***generators*** without using a function with the `yield` statement 
- It is syntactically ***similar*** to a **list comprehension**
- It uses parentheses `()` instead of square brackets `[]`
- Once a generator is consumed, it cannot be reused
- **generator expressions** are highly memory efficient for large datasets
- Instead of creating the whole list in memory, they generate items **one at a time** (lazily), which makes them more memory-efficient for large data sets
- When we iterate over a **generator object**, it computes each value **on the fly** and remembers where it left off.

> Unlike list comprehensions which construct and store an entire list in memory, generator expressions create an iterable that yields values on demand, making them highly memory-efficient, especially when dealing with large datasets or infinite sequences

> A list comprehension returns an iterable. It means that you can iterate over the result of a list comprehension again and again

However, a generator expression returns an iterator, specifically a lazy iterator. It becomes exhaused when we complete iterating over it
---
### Basic Syntax:
```Python
    (expression for item in iterable if condition)
```
---
### Key Characteristics of Generator Expressions and Reasons for using them

- Memory Efficiency
    - Avoids storing the entire sequence in memory, making it suitable for processing large amounts of data
- Faster for Large Data sets 
    - No need to hold all values in memory
- Handling infinite Sequences
- Concise Syntax
- Lazy evaluation
    - Values are generated one at a time, as needed
    - Values are generated and yielded only when requested during iteration, not all at once when the expression is defined
- Single-Use Iterators - Once exhausted, can't be reused
    - We can't reuse it after consumption
    - Once a generator expression has been iterated through and consumed, it cannot be reused. To iterate again, a new generator expression must be created
- Cannot be indexed 
    - We can't index a generator
    - Not subscriptable like lists

---
> Generator expressions generate values on the fly. This **lazy evaluation** significantly reduces memory consumption, making them ideal for processing large datasets or streams of data that cannot fit entirely in memory 

---
> Generator expressions offer a powerful way to create iterators that are memory efficient and performant particularly in scenarios where the full sequence does not need to be held in memory simultaneously

---
> Generator expressions in Python are used primarily for memory efficiency and performance optimizations when dealing with iterable sequences, especially large or potentially infinite ones

---
### Creation of Generator Objects
> A generator expression directly returns a generator object, which can then be iterated over 
- using a `for` loop 
    or
- by calling `next()` on it

---

## Key Concepts

- A **generator** is an iterator that yields items one at a time using a special syntax.
- **Generator expressions** look like list comprehensions but use **parentheses `()` instead of square brackets `[]`**.
- They **do not compute** the items until you iterate over them.
- They are **useful for large data sets**, streaming data, or any situation where creating the full list in memory is not optimal.

---
---

## Benefits of Generator Expressions

| Feature      | List Comprehension       | Generator Expression                 |
| ------------ | ------------------------ | ------------------------------------ |
| Syntax       | `[x for x in ...]`       | `(x for x in ...)`                   |
| Memory Usage | High (creates full list) | Low (lazy evaluation)                |
| Performance  | Fast for small lists     | Better for large/streaming data      |
| Reusability  | List can be reused       | Generator is exhausted after one use |

---