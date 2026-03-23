# The Dog class has two attributes - name and breed
# and one method bark()

class Dog:
    """A simple attempt to model a dog."""
    count = 0                       # Class variable to count instances
    species = "Canis familiaris"    # Class variable 
    def __init__(self, name, breed, age=1):
        """Initialize attributes."""
        # attributes 
        self.name = name    # Instance Variable
        self.breed = breed  # Instance Variable
        self.age = age
        Dog.count += 1      # Increment class variable
    # method
    def bark(self):
        print("Woof!")

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

# The special method __init__ is a constructor that is called when a new instance of the class is created

# The self parameter refers to the instance of the class and is used to access attributes and methods

# Creating objects (Instances)
dog1 = Dog("Sheru", "Pariah")
dog2 = Dog("Bruno", "Beagle")
dog3 = Dog("Simba", "Labrador", 2)

# Access the attributes of an object using dot notation
print(dog1.name)        # Output: Sheru
print(dog2.breed)       # Output: Beagle

# Call the method of an object
dog1.bark()             # Output: Woof!
dog3.sit()              # Output: Simba is now sitting.

# Modifying Class Variable
print(dog2.species)     # Output: Canis familiaris
Dog.species = "Canis lupus familiaris"      # Changing class variable
print(dog2.species)     # Output: Canis lupus familiaris

print(Dog.count)        # Output: 2
