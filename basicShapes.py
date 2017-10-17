

# lab03.py, Derek Wang
import turtle
import math

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.width(4)

def drawRectangle(width, height, tilt, penColor, fillColor):
    """
    draw a rectangle with a given width, height, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
    relative to the horizontal axis. After the rectangle is drawn, the turtle should return to its original position with an orientation of 0 degrees with respect to the x-axis.
    Use a turtle called t to create the drawing
    """
    t.seth(0)
    t.color(penColor, fillColor)
    t.left(tilt)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def drawTriangle(base, height, tilt, penColor, fillColor):
      angle = math.atan(height/base)*180/math.pi
      t.seth(tilt)
      t.color(penColor, fillColor)
      t.begin_fill()
      t.forward(base)
      t.left(180-angle)
      t.forward(math.sqrt(height**2+base**2))
      t.left(90+angle)
      t.forward(height)
      t.end_fill()
      t.seth(0)
   
if(__name__ == "__main__"):
    drawRectangle(100,100,23,"brown","orange")  # call the function to draw two rectangles of different sizes and colors
    t.up()     
    t.goto(0, -100)  
    t.down()
    drawTriangle(200,300,89,"purple","green")

