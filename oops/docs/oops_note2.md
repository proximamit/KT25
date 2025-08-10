# OOPS - Object-Oriented Programming System

### Class Variable  

A **class variable** is a variable that is shared by all instances of a class and used for storing data common to all instances of a class  

> It is a variable defined within the class, but outside of any methods

### Instance Variable  
> It is a variable that is unique to each instance of a class and used to store data that is specific to each instance of the class  

* It is a variable that is defined within the class, but inside a method  
* Accessed using the self keyword

## Types of Methods

1. Instance Methods  
2. Class Methods  
3. Static Methods  


## Access Specifiers (also known as Access modifiers)
1. Public - Fully Accessible 
2. Protected - Meant for internal/subclass use (not for public API use) - For Partial Encapsulation
3. Private - To support encapsulation (hide complex logic) - Not **directly** accessible from outside the class

**name** - public access specifier example (No underscore before the name)  
**_name** - protected access specifier example (One underscore before the name)  
**__name** - private access specifier example (Two underscores before the name)  

> Public access specifiers are intended to be accessible from outside the class  
---
> Protected and Private access specifiers are intended to be accessed only within the class  

---
