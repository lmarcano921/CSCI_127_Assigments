#Luis A Marcano
#11/10/2022
#luis.marcano29@myhunter.cuny.edu

#A program that uses multi-colored turtles
import turtle
t = turtle.Turtle()
t = turtle.Turtle(visible=False)

def petal(color, angle):
    
    turtle.colormode(255)   
    
    if color == "red" or color =="blue" or color =="yellow" or color =="purple" or color =="cyan":
        t.color(color)
    else:
        t.color("green")
        
    t.penup()
    t.left(angle)
    print(angle)
    t.pendown() 
    for y in range(0,255,10):
            t.forward(10)        #Move forward
            t.pensize(y)        #Set the drawing size to be i (larger each time)
            t.color(0,y,y)
    t.penup()
    t.pensize(0)  
    #t.backward(260)
    
           

        
def flower(color, petals):
    t.shape("turtle")
    pet = petals
    t.penup()
    angle = 360/petals
    col = color
    t.pendown()
    
    for i in range(1,pet+1):
        petal(col,angle*i)
        
    
    
def main():
    
    scn = turtle.Screen()
    flower("cyan",6)
    scn.exitonclick()

if __name__ == "__main__":
    main()