class Point:
    # In Python, a method starts with the def keyword
    # followed by a space, and the name of the method
    # This is followed by a set of parentheses
    # contining the parameter list
    # and terminated with a colon
    def reset(self):
        self.x = 0
        self.y = 0

# One difference between methods of classes and functions outside classes
# is that methods have one required argument conventionally named self

# the self parameter is also known as the instance variable
# the self argument to a method is a reference to the object
# that the method is being inovked on

p1 = Point()

p1.x = 7
p1.y = 6

print(p1.x, p1.y)
p1.reset()
print(p1.x, p1.y)
