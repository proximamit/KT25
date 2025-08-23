# Creating a list
fruits = ['apple', 'banana', 'cherry']
print(fruits)               # Output: ['apple', 'banana', 'cherry']
my_fav_fruit = fruits[0]

# Accessing elements
print(my_fav_fruit)        # Output: apple

# Modifying list
fruits[1] = 'blueberry'
print(fruits)               # Output: ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append('date')
print(fruits)               # Output: ['apple', 'blueberry', 'cherry', 'date']

# Slicing
available_fruits = fruits[1:3]
print(available_fruits)     # Output: ['blueberry', 'cherry']

# Removing elements
fruits.remove('cherry')
print(fruits)               # Output: ['apple', 'blueberry', 'date']