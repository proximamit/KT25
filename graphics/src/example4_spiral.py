import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")

# Draw a spiral
for i in range(25):
    t.forward(i * 10)  # Move forward
    t.right(45)         # Turn right by 45 degrees

turtle.done()  # Keeps the window open after drawing is done
