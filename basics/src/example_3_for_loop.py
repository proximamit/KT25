# For Loop - Basic example(s)

# Iterating through a list:
fruits = ["apple", "banana", "coconut", "grapes", 
          "guava", "mango", "orange", "papaya",
            "pomegranate", "pineapple", "water melon"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
  print(f"Index {index}: {fruit}")

# Iterating through a range of numbers:
for i in range(5):
    print(i)

# Iterating through a string:
word = 'python'
for char in word:
    print(char)

# Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Iterating through a dictionary:
person = {"name": "Mark", "age": 52, "city": "Toronto"}
for key, value in person.items():
    print(f"{key}: {value}")
