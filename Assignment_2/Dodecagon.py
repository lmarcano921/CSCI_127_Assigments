#Name: Luis Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 8/30/2022
#This program draws a dodecagon

import turtle

#object to pause the screen later
scn = turtle.Screen() 

#create a turtle object
turtle = turtle.Turtle()

#loop to draw the dodecagon
for i in range(12):
    turtle.forward(100)
    turtle.left(30)

#pauses screen to program doesn't close
scn.exitonclick()