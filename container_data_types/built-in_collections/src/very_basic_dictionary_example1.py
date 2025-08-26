# Creating a dictionary
my_car = {
    "brand": "Mahindra",
    "model": "XEV 9e",
    "year": 2025
}

# Accessing values
print(my_car["brand"])              # Output: Mahindra
print(my_car["year"])              # Output: 2025

# Modifying a value
my_car["year"] = 2024
print(my_car["year"])              # Output: 2024

# Adding a new key-value pair
my_car["price"] = "Rs 24.90 Lakh"
my_car["color"] = "Desert Myst"
# xev_colors = (Everest White, Ruby Velvet, Stealth Black, Deep Forest, Nebula Blue, 
#               Desert Myst, Tango Red)
print(my_car["price"])              # Output: Rs 24.90 Lakh
print(my_car["color"])              # Output: Desert Myst

print(my_car)
# Output: 
# {'brand': 'Mahindra', 'model': 'XEV 9e', 'year': 2024, 'price': 'Rs 24.90 Lakh', 'color': 'Desert Myst'}
print(len(my_car))                  # Output: 5

# Removing a key-value pair
my_car.pop("year")
my_car.pop("color")
print(my_car)
# Output: 
# {'brand': 'Mahindra', 'model': 'XEV 9e', 'price': 'Rs 24.90 Lakh'}
print(len(my_car))                  # Output: 3
print(type(my_car))                 # Output: <class 'dict'>

# Creating a dictionary using dict() constructor, using Keyword Arguments
new_car = dict(brand="Mahindra", colors=["Stealth Black", "Deep Forest", "Nebula Blue"])
print(new_car)
# Output: 
# {'brand': 'Mahindra', 'colors': ['Stealth Black', 'Deep Forest', 'Nebula Blue']}
print(new_car["colors"])            # Output: ['Stealth Black', 'Deep Forest', 'Nebula Blue']

# Trying to access values of a key that doesn't exist
#print(new_car["RoadTax"])
# KeyError: 'RoadTax'

# Creating an empty dictionary
neighbors_car = dict()

# Creating a dictionary from a list of tuples
mahindra_dealers = [
                    ("Neon Motors", "Chandanagar"),
                    ("VVC Motors", "Jubilee Hills"),
                    ("Landmark Mahindra", "Tellapur"),
                    ("Automotive Mahindra", "Punjagutta")
]
print(type(mahindra_dealers))                   # Output: <class 'list'>
print(type(mahindra_dealers[0]))                # Output: <class 'tuple'>
mahindra_dealers_dict = dict(mahindra_dealers)  # Output: <class 'dict'>
print(type(mahindra_dealers_dict))
print(mahindra_dealers_dict)
# Output: 
# {'Neon Motors': 'Chandanagar', 'VVC Motors': 'Jubilee Hills', 'Landmark Mahindra': 'Tellapur', 
# 'Automotive Mahindra': 'Punjagutta'}