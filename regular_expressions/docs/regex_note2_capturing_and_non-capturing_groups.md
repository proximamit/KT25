# Capturing and non-capturing groups in Regular Expressions

- In regular expressions, both capturing and non-capturing groups are used to group parts of a pattern
- The key difference lies in whether the matched text of the group is 
"captured" or "stored" for later retrieval or backreferencing

> A backreference in a regular expression allows us to match the exact same text that was previously 
> matched by a capturing group. 
---
Capturing groups are defined by enclosing parts of our regular expression in parentheses ()

- **Capturing groups** - When we use parentheses () in our regex pattern, the text matched by that part of
the pattern is `captured` and stored in a numbered group. 
- The first capturing group is 1, the second is 2, and so on based on the order of their opening parentheses from left to right

For capturing group - `()`
---

**Backreferencing** - To refer back to the content of a previously captured group within the same regular expression, we use a backslash followed by the group's number (e.g. \1 for group 1, \2 for group 2)

> group 0 refers to the entire match of the regular expression itself

---

**Non-Capturing group** - Does not capture the matched text. This means that the matched content of a 
non-capturing group cannot be accessed later as a separate group or used in backreferences

Defined by `(?: ...)`

> Used when we need to group parts of a pattern for structural purposes but do not need to extract or 
refer to the matched content of that specific group