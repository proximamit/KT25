import turtle
import random

def draw_rangoli_design(t, size, colors):
    for i in range(10): # Repeat the inner pattern 10 times
        t.pencolor(random.choice(colors)) # Use a random color
        for _ in range(4): # Draw a small shape (e.g., a square variation)
            t.forward(size)
            t.right(90)
        t.right(36) # Rotate for the next iteration

def main():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0) # Fastest drawing speed
    t.up()
    t.goto(0, -50) # Center the design
    t.down()

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    draw_rangoli_design(t, 100, colors)
    
    t.hideturtle()
    turtle.done() # Keep the window open until clicked

if __name__ == "__main__":
    main()

