import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")

# Draw a spiral
for i in range(35):
    t.forward(i * 10)  # Move forward
    t.right(45)         # Turn right by 45 degrees

# Instead of `turtle.done()`, use screen.mainloop()
screen.mainloop()  # Keeps the window open until the user manually closes it
