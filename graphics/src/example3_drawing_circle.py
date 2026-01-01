import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# Draw a circle
t.circle(50)  # Draw a circle with a radius of 50 units

turtle.done()  # Keeps the window open after drawing is done
