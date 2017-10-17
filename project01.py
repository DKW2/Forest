# project01.py, Derek Wang

from basicShapes import *
import random

def drawTree(height, color):
    
    ''' 
    This function draws a tree of a given height that consists of a rectangular brown bark and a top comprised of three triangles of a given color stacked on top of each other.
    The bottom left corner of the bark should be at current location of the turtle making no assumptions about the orientation of the turtle.
    After drawing the tree the turtle should be returned to its original position and oriented at 0 degrees 
    All other parameters such as the width of the tree and the length of the bark must be chosen so that the tree is well proportioned. 
    '''
    x = t.xcor()
    y = t.ycor()
    bark = height/15
    t.seth(0)
    drawRectangle(bark, height*2/5, 0, "brown", "brown")
    base = triangleBase(height)
    t.up()
    t.goto(x+bark/2, y+height*7/10)
    t.down()
    drawTriangle(base, base, -135, color, color)
    for i in range(2):
        t.up()
        t.goto(t.xcor(), t.ycor()+height*3/20)
        t.down()
        drawTriangle(base, base, -135, color, color)
    t.up()
    t.goto(x,y)
    t.down()
    t.seth(0)

def drawForest():
    ''' 
    Draws a collection of trees placed at random locations within a rectangular region
    '''
    t.up()
    t.goto(-400,0)
    t.down()
    y = t.ycor()
    shadesOfGreen =["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"] # A list of color codes for different shades of green
    for i in range(10 + random.randint(0, 5)):
        t.up()
        t.goto(t.xcor() + random.randint(50,75), y + random.randint(-50,50))  
        t.seth(0)
        t.down()
        drawTree(200 + random.randint(-100,100), random.choice(shadesOfGreen))
    
def checkTreeHeight():
    t.up()
    t.goto(0,100)
    t.down()
    drawRectangle(200, 200, 0 , "red","")
    t.seth(0)
    drawTree(200, "green")

def drawHut():
    '''
    Draw a brown hut of fixed dimensions purely composed of rectangles
    Use the random module to enhance your drawing by introducing irregularilities in a controlled way
    '''
    xori = t.xcor()
    yori = t.ycor()
    for i in range(14):
        x = t.xcor()
        y = t.ycor()
        randPos(x,y)
        drawRectangle(7.5,75,0, "black", "brown")
        t.goto(x,y)
        t.forward(5)
    t.up()
    t.goto(x-32.5, y+115)
    t.down()
    t.seth(0)
    
    for i in range(12):
        drawRectangle(75 + random.randint(-10,10),7.5, 210 + 10*i, "black", "brown")
    t.up()
    t.goto(xori,yori)
    t.down()
    t.seth(0)

def randPos(x,y):
    t.goto(x+random.randint(-2,2),y+random.randint(-2,2))
    
def drawVillage():
    '''
    Draw a sequence of five huts, placed randomly along a horizontal line
    '''
    t.up()
    t.goto(0-330, 0 - 100)
    t.down()
    y = t.ycor()
    for i in range(5):
        drawHut()
        t.up()
        t.goto(t.xcor()+ 150, y + random.randint(-20,20))
        t.down()
        
    
def triangleBase(height):
    return height*3*math.sqrt(2)/10

if __name__=="__main__":
    #drawTree(200, "green")
    #checkTreeHeight()
    drawForest()
    #drawHut()
    drawVillage()
    #regularPlay()

