# Example to show strings are immutable

greeting = "Hello, world!"
print(f"Original string: {greeting}")
print(f"Memory address of original string: {id(greeting)}")
# The id() function in Python returns the memory address of an object

# Attempting to change the first character (which is 'H') to 'C'
try:
    greeting[0] = 'C'
except TypeError as e:
    print(f"\nError: {e}")

# Creating a new string
new_greeting = 'C' + greeting[1:] 
print(f"New string: {new_greeting}")
print(f"Memory address of new string: {id(new_greeting)}")

# Using the .replace() method also creates a new string
replaced_greeting = greeting.replace('H', 'C')
print(f"Replaced string: {replaced_greeting}")
print(f"Memory address of replaced string: {id(replaced_greeting)}")

