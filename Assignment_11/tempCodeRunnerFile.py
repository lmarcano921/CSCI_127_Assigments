#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/26/2022
#This program draws 2 blobs of blue

import turtle                #Import the turtle drawing package
screen = turtle.Screen()
turtle.colormode(255)        #Allows colors to be given as 0...255
t = turtle.Turtle()        #Create a turtle

t.shape("turtle")        #Make it turtle shaped
t.penup()
t.backward(100)
t.left(90)
t.backward(100)
t.right(90) #you fill in a degree in ??
t.pendown()       

#Move her backwards, to give more space to draw
#For 0,10,20,...,250
for i in range(0,255,10):
    t.forward(10)        #Move forward
    t.pensize(i)        #Set the drawing size to be i (larger each time)
    t.color(0,i,i)        #Set the red channel to be i (brighter each time)

t.penup()
t.pensize(0)
t.goto(0,0)
t.left(180)
t.forward(100)
t.left(90)
t.forward(100)
t.right(180)
t.pendown()

for i in range(0,255,10):
    t.forward(10)        #Move forward
    t.pensize(i)        #Set the drawing size to be i (larger each time)
    t.color(0,i,i)        #Set the red channel to be i (brighter each time)

screen.exitonclick()