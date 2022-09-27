#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/26/2022
#This program draws 2 blobs of blue

import turtle
turtle.colormode(255)
scn = turtle.Screen()
turtle = turtle.Turtle()

turtle.shape("turtle")
turtle.pendown()
#turtle.backward(100)

for i in range(0,255,10):
    turtle.forward(10)
    turtle.pensize(i)
    turtle.color(0,i,i)
    
turtle.penup()
turtle.setpos(0,0)
turtle.left(90)
turtle.color(0,0,0)
turtle.pendown()
size = turtle.pensize(0)

for i in range(0,255,10):
    turtle.forward(10)
    turtle.pensize(i)
    turtle.color(0,i,i)
     
scn.exitonclick()