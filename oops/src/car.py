class Car:
    def __init__(self, make, model, year):
        # attributes
        self.make = make
        self.model = model
        self.year = year

    def honk(self):
        print("Beep beep!")

# Create an object of the Car class
my_car = Car("Toyota", "Innova", 2025)

# Access attributes of the object 
print(my_car.make)
print(my_car.model)
print(my_car.year)

# Call a method of the object
my_car.honk()
