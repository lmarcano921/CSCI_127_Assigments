#Name: Luis Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 8/30/2022
#This program draws a flower

import turtle

scn = turtle.Screen()
turtle = turtle.Turtle()

for i in range(9):
    turtle.forward(100)
    turtle.left(105)
    turtle.forward(52)
    turtle.left(105)
    turtle.forward(100)
    turtle.right(170)
    
scn.exitonclick()