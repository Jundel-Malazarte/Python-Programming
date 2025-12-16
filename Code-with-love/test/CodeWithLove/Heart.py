import turtle

def draw_heart():
    # Draw a heart shape
    heart = turtle.Turtle()
    heart.speed(3)
    heart.color("red")
    heart.fillcolor("red")
    
    heart.penup()
    heart.goto(-50, 0)  # Center the heart horizontally
    heart.pendown()

    # Start filling the heart
    heart.begin_fill()

    # Draw the heart shape
    heart.left(140)
    heart.forward(180)  # Left side of the heart
    heart.circle(-90, 200)  # Left curve
    heart.setheading(60)  # Adjust angle for right side
    heart.circle(-90, 200)  # Right curve
    heart.forward(180)  # Right side of the heart

    # End filling the heart
    heart.end_fill()
    heart.hideturtle()

def draw_I():
    # Draw the letter "I"
    pen = turtle.Turtle()
    pen.speed(3)
    pen.penup()
    pen.goto(-260, 150)  # Adjusted position for "I" to align with the heart
    pen.pendown()
    pen.color("black")
    pen.pensize(10)

    # Vertical line for "I"
    pen.setheading(90)
    pen.backward(110)
    pen.forward(220)
    pen.backward(110)

    pen.hideturtle()

def draw_U():
    # Draw the letter "U"
    pen = turtle.Turtle()
    pen.speed(4)
    pen.penup()
    pen.goto(150, 250)  # Adjusted position for "U" to align closer to the heart
    pen.pendown()
    pen.color("black")
    pen.pensize(10)

    # Draw vertical line and curve for "U"
    pen.setheading(270)
    pen.forward(140)
    pen.circle(60, 180)  # Bottom curve
    pen.forward(140)

    pen.hideturtle()

# Main drawing function
def draw_I_heart_U():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("I ❤ U")

    # Draw the components
    draw_I()
    draw_heart()
    draw_U()

    # Keep the window open
    screen.mainloop()

# Call the main function
draw_I_heart_U()