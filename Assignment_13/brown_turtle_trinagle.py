#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/27/2022
#This program draws a brown triangle with 3 turtles

import turtle                #Import the turtle drawing package
screen = turtle.Screen()
t = turtle.Turtle()        
t.shape("turtle")        
t.color("#0000CD")

t.penup()
t.backward(100)
t.pendown() 
t.forward(500)


#Move her backwards, to give more space to draw
#For 0,10,20,...,250
for i in range(0,255,10):
    t.forward(10)        #Move forward
    t.pensize(i)        #Set the drawing size to be i (larger each time)
    t.color(i,0,i)        #Set the red channel to be i (brighter each time)