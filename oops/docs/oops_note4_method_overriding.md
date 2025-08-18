# Method Overriding

- Method overriding in Python occurs when a **child class** defines a method that has the **same name and parameters** as a method in its **parent class**
- The child class method **overrides** or replaces the parent class method when called on an instance of the child class

> Method Overriding allows the **child class** to ***customize*** or **extend the behavior** of the **parent class** method
---
## What is Method Overriding in Python?

- **Method Overriding** in Python is a feature of Object-Oriented programming that allows a **child class(subclass)** to provide a ***specific implementation*** for a method that is **already defined** in its **parent class (superclass)**.
- When a method is overridden, the version in the subclass takes precedence over the version in the superclass when called on an object of the subclass  
- The method in the child class **has the same name, parameters, and signature** as the method in the parent class
- It allows a child class to **customize of completely replace** the behavior of a parent class method

> A **method signature** refers to the ***method name*** along with the **number and type of parameters** it takes

- the signature includes
    - The **method** name
    - The **number of arguments** (Parameter count)
    - The **order of arguments** (Parameter order, whether they are positional, keyword or variable arguments)
    - The **types of arguments** (Type hints are ***optional*** in Python, as Python is dynamically typed)
    - **Default Values**
- In Python, the ***return type*** of a method or function is not considered part of its signature 
---
## Why use Method Overriding?

- To provide ***specialized behavior*** in a child class
- To **extend or modify** the functionality if a parent class
- Helps implement **polymorphism**, where the same method behaves differently depending on the object type

---
### Key aspects of method overriding

- **Inheritance** - Method overriding is only possible within an inheritance hierarchy, where a subclass inherits from a superclass  

- **Same Method Signature** - The method in the subclass must have the same name and the same number of parameters as the method it overrides in the superclass  

- **Polymorphism** - Method overriding is a form of runtime polymorphism, meaning that the specific method 

- Use of `super()` - The `super()` function can be used to call the parent class's method from the child class if needed, allowing for extension of functionality rather than complete replacement

- **Customization** - It allows Child class to provide their own specialized behavior for methods inherited from their parent class, while still maintaining the same method name for consistency

### Rules to Remember

- Method names and parameters must be the **same** in both parent and child classes
- We can use `super()` to **invoke the parent method** if needed
- Overriding happens **only in inheritance** scenarios
- If the child class **does not override**, the **parent method is used**
