class Airplane:
    def __init__(self, model, manufacturer, speed, altitude, capacity):
        # Constructor to initialize the attributes of the Airplane class
        self.model = model
        self.manufacturer = manufacturer
        self.speed = speed
        self.altitude = altitude
        self.capacity = capacity
    
    # Method to simulate the airplane flying
    def fly(self):
        print(f"The {self.model} is now flying at an altitude of {self.altitude} meters.")
    
    # Method to simulate the airplane landing
    def land(self):
        print(f"The {self.model} has landed.")
    
    # Method to simulate accelerating the airplane
    def accelerate(self):
        self.speed += 100  # Increase speed by 100 km/h
        print(f"The {self.model} is accelerating. New speed: {self.speed} km/h.")
    
    # Method to simulate decelerating the airplane
    def decelerate(self):
        self.speed -= 100  # Decrease speed by 100 km/h
        if self.speed < 0:
            self.speed = 0  # Prevent negative speed
        print(f"The {self.model} is decelerating. New speed: {self.speed} km/h.")
    
    # Method to get the details of the airplane
    def get_details(self):
        return f"Airplane Model: {self.model}, Manufacturer: {self.manufacturer}, Capacity: {self.capacity} passengers."

# Example usage
if __name__ == "__main__":
    # Creating an instance of the Airplane class
    airplane1 = Airplane("Boeing 747", "Boeing", 600, 10000, 200)
    
    # Displaying details of the airplane
    print(airplane1.get_details())
    
    # Simulating airplane operations
    airplane1.fly()
    airplane1.accelerate()
    airplane1.decelerate()
    airplane1.land()
