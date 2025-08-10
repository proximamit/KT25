# The Dog class has two attributes - name and breed
# and one method bark()

class Dog:
    count = 0                       # Class variable to count instances
    species = "Canis familiaris"    # Class variable 
    def __init__(self, name, breed):
        # attributes 
        self.name = name    # Instance Variable
        self.breed = breed  # Instance Variable
        Dog.count += 1      # Increment class variable
    # method
    def bark(self):
        print("Woof!")

# The special method __init__ is a constructor that is called when a new instance of the class is created

# The self parameter refers to the instance of the class and is used to access attributes and methods

# Creating objects (Instances)
dog1 = Dog("Sheru", "Pariah")
dog2 = Dog("Bruno", "Beagle")

# Access the attributes of an object using dot notation
print(dog1.name)        # Output: Sheru
print(dog2.breed)       # Output: Beagle

# Call the method of an object
dog1.bark()             # Output: Woof!

# Modifying Class Variable
print(dog2.species)     # Output: Canis familiaris
Dog.species = "Canis lupus familiaris"      # Changing class variable
print(dog2.species)     # Output: Canis lupus familiaris

print(Dog.count)        # Output: 2
