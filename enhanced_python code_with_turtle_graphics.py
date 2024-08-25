### Enhanced Python Code with Turtle Graphics

The following code enhances the original Python script by adding more functionality and structure. It also includes comments for better understanding.

```python
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Enhanced Turtle Graphics")
screen.bgcolor("black")

# Create a turtle named 'pen'
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)

# Function to draw a cube
def draw_cube(side_length):
    pen.fillcolor('yellow')
    pen.begin_fill()
    for _ in range(4):
        pen.forward(side_length)
        pen.left(90)
    pen.end_fill()

# Function to draw a star
def draw_star(size):
    pen.fillcolor('blue')
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

# Main function to draw the entire scene
def draw_scene():
    pen.penup()  # Move without drawing
    pen.goto(-100, 0)  # Move to the starting position
    pen.pendown()  # Start drawing

    # Draw a square
    draw_square(100)

    # Move to the next position
    pen.penup()
    pen.goto(100, 0)
    pen.pendown()

    # Draw a cube
    draw_cube(100)

    # Move to the next position
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()

    # Draw a star
    draw_star(100)

# Call the main function
if __name__ == '__main__':
    draw_scene()
    turtle.done()
