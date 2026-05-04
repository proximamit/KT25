# *args and **kwargs

- `*args` and `**kwargs` are tools for creating flexible functions that can accept a variable number of arguments

- `*args` and `**kwargs` are powerful tools for designing flexible, extensible, and clean APIs.

- `*args` and `**kwargs` are used in Functions and Methods
- `*args` and `**kwargs` are used to accept arbitrary arguments.
- They turn rigid function signatures into adaptable interfaces
- We can use any name we want, like *values or **options instead of
`*args` and `**kwargs`. However, it is the standard convention to use `*args` and `**kwargs` names
---

## *args (Positional Variable Arguments)

`*args` collects positional arguments

- `*args` - Used for variable positional arguments

- `*args` collects extra positional arguments into a tuple

- `*args` is useful when designing extensible APIs or middleware
where the number of positional inputs isn’t fixed,
especially in decorators and function forwarding

- `*args` is useful when:
    - order matters
    - number of inputs varies

---

## **kwargs  (Keyword Variable Arguments)

- `**kwargs` - Used for variable keyword arguments

- `**kwargs` - Collects extra named arguments into a dictionary

- `**kwargs` is useful when:
    - inputs are named
    - optional
    - potentially large in number
