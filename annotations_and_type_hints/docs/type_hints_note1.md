# Type Hints and Annotations


## Type Hints

- Type hints are **Optional** and *Not Enforced*
- Type hints allow developers to explicitly declare the expected data types of 
variables, function arguments, and return values. 
- They serve as a form of documentation.
- They are primarily used by third-party static analysis tools and IDEs 
to detect potential type-related errors before the code is run
- They make code more readable and maintainable, especially in large projects
- Type hints = "this is what we expect"
- Type hints = optional, static guidance
- The Python interpreter itself does not enforce the type hints at runtime.

### Type Hints - Basic Syntax

- Append a **colon** and the **type name** to the variable or argument name.
- Use `-> Type` for function return values. 
---

## Type Hints and Annotations

- **Annotations** and **type hints** in Python are closely related

- All type hints are annotations, but not all annotations are type hints.
- Type hints = a specific use of annotations
- Type hints = a convention using annotations specifically for types
- **Annotations** = general-purpose metadata
- Annotations/type hints *do not change* **duck typing**

--- 
- Type hints say "You should use these types… but I won’t force you."
- Type Hints are a specific application of annotations. 
- While an annotation can be any expression (a string, a list, a class),
 a type hint uses that space to declare the expected data type.
 - Static type checkers, such as mypy or Pyright, can be used to analyze code 
 based on the type hints to identify potential type mismatches before the code 
 is run

---

## Duck Typing

Duck Typing refers to the idea that 
**the type of an object is determined by its behavior** 
(i.e. *what methods and attributes it has*)
rather than by its explicit class or inheritance hierarchy.

---
### What is duck typing in Python?

**Duck typing** is a concept where Python decides whether an object is usable 
based on **what it can do**, not **what it is**.

It comes from the idea:

> "If it looks like a duck, walks like a duck and quacks like a duck, it’s a 
duck."

In Python terms:
If an object has the required methods/behavior, it’s valid—no matter its actual 
type.

- Python always follows duck typing at runtime, regardless of annotations or 
type hints.

- Duck typing = "if it works, it’s valid"
- Duck typing = dynamic, runtime behavior
- **Duck typing** = "Don't ask what class it is, ask what it can do."
- Duck typing does not depend on annotations
- Annotations/type hints do not change duck typing

---

## Annotations

- Annotations = general metadata storage
- Annotations = "extra metadata (types or otherwise)"

---

## Statically Typed Language vs Python (Dynamically Typed)

- Static typing = strict, safe, caught early
- Statically typed language says "Tell me the type first, or I won’t run."
- Dynamic typing (Python) = flexible, but riskier at runtime

| Feature          | Statically Typed Languages | Python                     |
| ---------------- | -------------------------- | -------------------------- |
| Type checking    | Compile-time               | Runtime                    |
| Variable types   | Fixed                      | Flexible                   |
| Type errors      | Early detection            | May occur during execution |
| Type annotations | Required                   | Optional                   |
| Enforcement      | Strict                     | Not enforced by default    |

---
