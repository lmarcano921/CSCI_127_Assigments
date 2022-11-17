#Luis A Marcano
#11/10/2022
#luis.marcano29@myhunter.cuny.edu

#A program that uses multi-colored turtles
import turtle

def petal(color, angle):
    
    t = turtle.Turtle()
    t = turtle.Turtle(visible=False)
    #turtle.colormode(255)   
    
    if color == "red" or color =="blue" or color =="yellow" or color =="purple" or color =="cyan":
        t.color(color)
    else:
        t.color("green")

    t.shape("turtle")        #Make it turtle shaped
    t.penup()
    t.left(angle)
    t.pendown()       
    
    for y in range(0,256,10):
        t.forward(10)        #Move forward
        t.pensize(y)        #Set the drawing size to be i (larger each time)
        #t.color(y,0,y)  
            
    
    
def flower(color, petals):
    pet = petals
      
    angle = 360/petals
    col = color
    for i in range(1,pet+1):
        petal(col,angle*i)
    
def main():
    scn = turtle.Screen()
    col = "magenta"
    pet = 9
    flower(col,pet)
    scn.exitonclick()

if __name__ == "__main__":
    main()