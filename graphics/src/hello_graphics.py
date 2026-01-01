import turtle

# Create a screen and a turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Set colors and start filling
t.color("blue", "yellow")
t.begin_fill()

# Draw the square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Stop filling the shape
t.end_fill()

# Keep the window open until clicked
screen.exitonclick()
