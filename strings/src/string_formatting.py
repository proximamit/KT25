x = 10
name = "Jackie"
age = 6


# f-Strings - best and now most widely used method

print(f"{x=}")  #Output:  x=10

print(f"My dog's name is {name} and it is {age} years old")

# 
print(f"{name:>10}")  # right aligned
print(f"{name:<10}")  # left aligned
print(f"{name:^10}")  # center aligned


# 
print("Hello {}, you look {} years old".format(name, age))


# Oldest method for Python String Formatting  (using % operator)

print("My dog's name is %s and it is %d years old" % (name, age))