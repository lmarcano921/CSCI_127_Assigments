#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

import turtle 
import math

#recursive function to draw a pantegon
def drawPantegon(t, length, numEdges):
    if numEdges > 0:
        t.forward(length) #the turtle object, t, forward length steps
        t.left(72)# turn left 72 degrees
        drawPantegon(t, length, numEdges-1) #call drawPantegon with t, length, and numEdges-1

#pseudocode of cornerPantegon, which draws pantegon nested in left corner.
def cornerPantegon(t, length):
   if length >= 25:
        drawPantegon(t, length,5)
        length = length//2 #reduced length by half (use integer division in this function)
        cornerPantegon(t, length)#call cornerPantegon with t and length, that is, draw a pantegon with t and updated length

def nestedPantegon(t, length):
    if length >= 25:
        #1. call drawPantegon with t, length, and 5
        drawPantegon(t, length,5)
        #2. Turtle t moves forward length/2
        t.forward(length/2)
        #3. Turtle t turns left 36 degrees
        t.left(36)
        #4. call nestedPantegon with t, length * math.sin(54/180 * math.pi). To use sin function from math library, need to import math.
        nestedPantegon(t, length * math.sin(54/180 * math.pi))

def main():
    length1 =200
    length2 = 50
    t = turtle.Turtle()
    #cornerPantegon(t, length1)
    #drawPantegon(t,length1, 5)
    nestedPantegon(t, length2)
    #nestedPantegon(t, length1)

if __name__ == '__main__':
   main()