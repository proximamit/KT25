import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("red")

# Draw a star
for _ in range(5):
    t.forward(100)  # Move forward
    t.right(144)    # Turn right by 144 degrees to create star points

turtle.done()  # Keeps the window open after drawing is done
