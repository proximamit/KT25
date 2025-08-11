# Single Inheritance 

class Animal:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        # Calling parent class constructor using super()
        super().__init__(name)
        self.age = age

    def display_info(self):
        print(f"{self.name} is {self.age} years old.")

    # Method Overriding
    def speak(self):
        return f"{self.name} barks!"

class Cat(Animal):
    # Method Overriding
    def speak(self):
        return "Meow!!"

# # Creating an object of Child Class - Dog
my_dog = Dog("Jackie", 4)

# Method from parent class
my_dog.greet()                  # Output: Hello, Jackie

print(my_dog.speak())           # Output: Jackie barks!

# Method from child class
my_dog.display_info()           # Output: Jackie is 4 years old.

neighbors_cat = Cat("Kitty")
print(neighbors_cat.speak())    # Output: Meow!!
