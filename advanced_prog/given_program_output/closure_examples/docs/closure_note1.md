# Closure - A function with a Memory

- A **closure** in Python is a function object that **remembers values from its enclosing scope even after that scope has finished executing**.

- In other words,
a **closure** is a function object that **remembers values** in the enclosing scope even if those values are no longer in memory. 
- It happens when a nested function references a variable from its outer function. 

---

## Closures are built on the following 3 rules:

1. **Nested functions** — a function inside another function
2. **Free variables** — variables from the outer function used by the inner function
3. **Returning inner function** - The enclosing function must return the nested function. 

### A function is a closure when it meets the above 3 specific criteria


- **Function objects carrying state** — the inner function "remembers" those variables

---

## How Closures Work

- When Python creates `inner`, it stores references to variables used from the outer scope.

- The variable is not copied into the function body textually. 
- Instead, Python keeps a hidden environment attached to the function object.

---

### Decorators heavily rely on closures

---

### Multiple Closures from same Function maintain separate environments

---

### Closures are fundamental in functional programming

---
