# 

text = "Python"

print("\nZero based Indexing: \n")
print(text[0])  # P
print(text[1])  # y
print(text[5])  # n
print("\nNegative Indexing: \n")
# Negative Indexing
print(text[-6])  # P
print(text[-1])  # n
print(text[-2])  # o

# Basic Slicing

print("\nBasic Slicing: \n")
print(text[0:3])  # Pyt
print(text[2:5])  # tho

# Omitting Start or Stop
print("\nOmitting Start or Stop: \n")
print(text[:4])   # Pyth  (start = 0)
print(text[2:])   # thon  (go till end)
print(text[:])    # Python (full string)

# Using Step
print("\nUsing Step\n")
print(text[0:6:2])  # Pto
print(text[::2])    # Pto


# Reversing a String
print("\nReversing a String\n")
print(text[::-1])  # nohtyP

# Looping through a String
print("\nLooping through a String")

for x in "Pineapple":
  print(x)

# String Concatenation 
## Using the + operator to combine two or more strings
cat = "Tom"
mouse = "Jerry"
entertainment = cat + " and " + mouse
print(entertainment)

# Repetition
## Using the * operator with an integer to repeat a string multiple times.
print("=" * 13)