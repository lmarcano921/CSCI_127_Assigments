#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/27/2022
#This program draws shades of purple

import turtle                #Import the turtle drawing package
screen = turtle.Screen()
turtle.colormode(255)        #Allows colors to be given as 0...255
t = turtle.Turtle()        #Create a turtle

t.shape("turtle")        #Make it turtle shaped
t.penup()
t.backward(100)
t.pendown()       

#Move her backwards, to give more space to draw
#For 0,10,20,...,250
for i in range(0,255,10):
    t.forward(10)        #Move forward
    t.pensize(i)        #Set the drawing size to be i (larger each time)
    t.color(i,0,i)        #Set the red channel to be i (brighter each time)

for i in range(255,0,-10):
    t.forward(10)        #Move forward
    t.pensize(i)        #Set the drawing size to be i (larger each time)
    t.color(i,0,i)        #Set the red channel to be i (brighter each time)