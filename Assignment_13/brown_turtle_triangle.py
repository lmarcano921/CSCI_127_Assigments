#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/27/2022
#This program draws a brown triangle with 3 turtles

import turtle
screen = turtle.Screen()
turtle.colormode(255)
t = turtle.Turtle()        
t.color(150, 75, 0)
t.shape("turtle")
t.penup()
t.backward(100)
t.pendown()



#Move her backwards, to give more space to draw
#For 0,10,20,...,250
for i in range(3):
    t.forward(100)       #Move forward
    t.left(120)        #Set the drawing size to be i (larger each time)
    t.stamp()      #Set the red channel to be i (brighter each time)