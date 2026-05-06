# if __name__ == "__main__":

The above construct (a basic building block) is essential for separating script behavior from module behavior.

---

The purpose of a Python file can be (to use as) :

- Executable script (test code, main logic)
- Reusable module (functions, classes)

i.e. 

- We can directly run a `.py` file (as a Python Script)
- or We can Import a python file as a module

---

## This construct checks if this file being run directly, and not imported

--- 
## Every Python file (module) has a special built-in variable called __name__

- if __name__ == "__main__":
    - Runs code (below it ) only when file is executed directly
    - Prevents code from running when imported

## Used for 
- Testing code
- Entry point for programs
- Prevent unwanted execution


### Example usage as Entry point for programs

```python
def main():
    # main logic here
    pass

if __name__ == "__main__":
    main()
```

---

## How Python sets `__name__`

When Python runs a file:

- For the **first/main file** `__name__ = "__main__"`
- For imported modules `__name__ = module_name`