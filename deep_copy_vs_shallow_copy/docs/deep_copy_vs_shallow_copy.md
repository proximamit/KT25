# Deep Copy vs Shallow Copy

### When it matters?:

## In Python, the concept of **deep** and **shallow** copies primarily becomes relevant when we are working with **mutable objects** that contain other **mutable objects**.

The need for deep vs. shallow copying arises only when:

1. **Nested mutable objects** are involved (e.g., lists inside lists, dictionaries inside dictionaries).
2. We want to **avoid side effects** where changes in one object affect another due to shared references in the nested structures.
---
### Why It Matters:

* **Shallow copies** are often sufficient when the objects we are working with don't contain nested mutable objects  
or  
when we don't need to preserve complete independence between the original and copied objects.  

* **Deep copies** are necessary when we need to ensure that the new object is entirely independent, including its nested structures, from the original object.
---
## Shallow Copy
- **shallow copies** are faster and sufficient for simpler cases
- If an object is flat (i.e., it doesn't contain nested mutable objects), a shallow copy works just fine because there are no references to worry about.
- A shallow copy of an object creates a new object, but the contents inside that object (if they are mutable) are not copied—they are simply referenced.  
This means that the new object shares references to the same inner objects as the original one.  
- With a shallow copy, modifying a nested object inside the copied object will affect the original object as well because both objects point to the same nested object.
---
## Deep Copy
- **deep copies** are necessary when working with complex, nested mutable structures where full independence between copies is required.
- A deep copy creates a completely new object with new copies of all the nested objects within it.
- With deep copy, there are no shared references to mutable objects between the original and the copied version.
