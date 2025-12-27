# Python Basics

- Python source code is clean to write and **read**
- Scoping in Python is determined by **indentation**
- `#` is used for comments in Python (until the end of the line)
- a conditional statement (like if statement) ends with a colon followed by a group of indented statements

---

## Keywords

### 1. **Control Flow Keywords**

- **if**: Conditional statement (used for decision-making).
- **elif**: Else-if, used in conditional statements.
- **else**: The else clause in conditional statements.
- **for**: For loops, used for iterating over a sequence.
- **while**: While loop, used for iteration based on a condition.
- **break**: Exits the current loop. **Stops the loop entirely.**
- **continue**: Skips the current iteration of a loop and continues to the next one.
- **pass**: A placeholder that does nothing (used to create empty blocks of code).

### 2. **Keywords related to Functions**

- **def**: Used to ***define a function***.
- **return**: Returns a value from a function.
- **lambda**: Defines an anonymous function (lambda function).
- **yield**: Used to generate a value from a generator function.
- **global**: Declares a global variable inside a function.
- **nonlocal**: Refers to a variable in the nearest enclosing scope, excluding global scope.

### 3. **Keyword related to Object-Oriented Programming**

- **class**: Used to define a class.

### 4. **Keywords related to Exception Handling**

- **try**: Used to catch exceptions.
- **except**: Defines the block of code to execute if an exception occurs.
- **finally**: Executes after the try-except block, regardless of exceptions.
- **raise**: Raises an exception explicitly.

### 5. **Keywords related to Operators**

- **and**: Logical AND operation.
- **or**: Logical OR operation.
- **not**: Logical NOT operation.
- **in**: Checks if a value is contained within an iterable (list, string, etc.).
- **is**: Checks if two variables point to the same object. (Compares object identity)

### 6. **Keywords related to Modules**

- **import**: Imports a module.
- **from**: Imports specific elements from a module.
- **as**: Renames an imported module or element.
- **del**: Deletes a variable or object. (Deletes a reference to a module or element)

### 7. **Keywords related to Values**

- **True**: Boolean value representing truth.
- **False**: Boolean value representing false.
- **None**: Represents the absence of a value or null value.

### 8. **Keyword related to Context Manager**

- **with**: Used to wrap the execution of a block of code within methods defined by a context manager (for example, file operations).
In other words,
Used to simplify exception handling and resource management, specifically when dealing with context managers
The with statement makes it easier to manage resources by ensuring that they are properly cleaned up after use, even if an error occurs within the block.

### 9. **Keywords related to Asynchronous Programming**

- **async**: Marks a function or method as asynchronous. 
In other words, Used to define a coroutine (asynchronous function).
- **await**: Pauses the execution of an asynchronous function until a result is returned.
Used inside an asynchronous function to pause execution until a result is available, allowing other tasks to run.

### 10. **Keyword primarily used for debugging**

- **assert**: Used to test a condition (often for debugging).

---

## Soft Keywords

### Soft Keywords- only act as keywords in specific contexts

- **match**
- **case**
- **_** (underscore): acts as a wildcard, matching anything
- **type** 

---

The **match/case** statements provides a more readable alternative to complex if/elif/else chains


**type** soft keyword is used to declare generic type aliases
In other words,
Used to explicitly define generic type aliases in the context of 
type hints or type annotations.

---
