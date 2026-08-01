# Defining the Class
class Car:
    # initialize attributes
    def __init__(self, brand, color):
        self.brand = brand  # Instance attribute
        self.color = color  # Instance attribute

    # Instance method
    def start_engine(self):
        return f"The {self.color} {self.brand} is starting. Vroom!"

# Creating Objects (Instantiation)
car1 = Car("Toyota", "Red")
car2 = Car("Tesla", "Blue")

# Accessing attributes and methods
print(car1.brand)          # Output: Toyota
print(car2.color)         # Output: Blue
print(car1.start_engine())  # Output: The Red Toyota is starting. Vroom!
