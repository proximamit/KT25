import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)  # Fast drawing speed
t.width(2)

# Function to draw a petal (an arc-like shape)
def draw_petal():
    for _ in range(2):
        t.circle(100, 60)  # Draw the arc part of the petal
        t.left(120)  # Turn to form the symmetrical petal

# Function to draw a flower using petals
def draw_flower():
    for _ in range(6):
        draw_petal()
        t.left(60)  # Rotate to draw the next petal

# Function to draw a dot in the center
def draw_center_dot():
    t.penup()
    t.goto(0, -20)  # Position for the center dot
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(20)  # Draw a small circle in the center
    t.end_fill()

# Function to draw lines radiating from the center
def draw_lines():
    t.penup()
    for _ in range(12):  # 12 lines to create a star-like effect
        t.goto(0, 0)
        t.setheading(_ * 30)  # Set heading for each line
        t.forward(100)
        t.pendown()
        t.forward(50)
        t.penup()
        t.backward(150)

# Function to write the "Happy New Year 2026" message
def write_message():
    t.penup()
    t.goto(0, -200)
    t.color("black")
    t.write("Happy New Year 2026", align="center", font=("Arial", 24, "bold"))

# Draw the Rangoli pattern
draw_flower()  # Draw flower pattern with petals
draw_center_dot()  # Draw center dot
draw_lines()  # Draw lines radiating from the center

# Write the message in the center
write_message()

# Finish up
screen.mainloop()  # Keeps the window open until the user closes it
