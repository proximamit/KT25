#  Mutable default argument trap

In Python, default arguments are evaluated once at function definition time.  
If the default is mutable and gets modified, the modified object persists across future function calls.  
The standard fix is using `None` and creating the mutable object inside the function.

---

- It happens because **default argument values are evaluated only once**, at function definition time — not every time the function is called
- That means if the default value is mutable (like a list, dict, or set), changes persist across calls.

---

## Best Practices

- Never use mutable objects as defaults
- Use sentinel values
- Use default_factory in dataclasses
- Be careful with nested mutable structures

---

### Think of default arguments as:

"Created once when the function is defined."

NOT:

"Created every time the function is called."

---

### Summary

The mutable default argument trap exists because:

- Python evaluates defaults once
- Mutable objects persist
- Mutating them affects future calls

The safe rule is:

> Never use mutable objects as default function arguments unless we intentionally want shared state.

---
