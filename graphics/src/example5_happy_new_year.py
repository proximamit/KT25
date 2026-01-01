import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)  # Fast drawing speed
t.width(2)

# Function to draw a circle with a given color and radius
def draw_circle(color, radius, position):
    t.penup()
    t.goto(position)  # Position the turtle
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a Rangoli pattern (a series of circles)
def rangoli_pattern():
    colors = ["red", "yellow", "green", "blue", "purple", "orange"]
    radius = 100
    for i in range(6):
        draw_circle(colors[i % len(colors)], radius, (0, -radius))
        radius += 20  # Increase the radius for next circle

# Function to write the "Happy New Year 2026" message
def write_message():
    t.penup()
    t.goto(0, -30)
    t.color("black")
    t.write("Happy New Year 2026", align="center", font=("Arial", 24, "bold"))

# Draw the Rangoli pattern
rangoli_pattern()

# Write the message in the center
write_message()

# Finish up
screen.mainloop()  # Keeps the window open until the user closes it
