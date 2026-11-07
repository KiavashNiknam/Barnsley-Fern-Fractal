# Kiavash Niknam
import turtle
import random

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Barnsley Fern Fractal")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

# Initial coordinates
x = 0
y = 0

# Get number of points
n = int(input("Enter number of points: "))

# Disable animation for faster drawing
screen.tracer(0)

# Barnsley Fern algorithm
for i in range(n):

    r = random.random()

    if r < 0.02:
        new_x = 0.50
        new_y = 0.27 * y

    elif r < 0.17:
        new_x = -0.14 * x + 0.26 * y + 0.57
        new_y = 0.25 * x + 0.22 * y - 0.04

    elif r < 0.30:
        new_x = 0.17 * x - 0.21 * y + 0.41
        new_y = 0.22 * x + 0.18 * y + 0.09

    else:
        new_x = 0.78 * x + 0.03 * y + 0.11
        new_y = -0.03 * x + 0.74 * y + 0.27

    # Update coordinates
    x = new_x
    y = new_y

    # Draw point
    t.goto(x * 250 - 150, y * 250 - 250)
    t.dot(2, "green")

# Update screen
screen.update()

# Keep window open
turtle.done()
