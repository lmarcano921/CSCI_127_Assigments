#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 8/30/2022
#This program draws 5 squares

import turtle
scn = turtle.Screen()
turtle = turtle.Turtle()

#switch case to allow the color change in the loop
def turtlecolor(i):
        switch = {
            0: "green",
            1: "blue",
            2: "cyan",
            3: "red",
        }
        return switch.get(i,"invalid input")

#sets the size of the pen for the shape
turtle.pensize(5)
#guess this changes the turtle into a circle
turtle.shape("circle")

#first loop to set the pen color and the long line
for i in range(4):
    
    #sets the color for the pen
    turtle.color(turtlecolor(i))
    turtle.forward(200)
    
    #second loop for the smaller square shape
    for y in range(3):
        turtle. forward(100)
        turtle.right(90)
    
scn.exitonclick()