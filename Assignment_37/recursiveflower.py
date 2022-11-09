#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

import turtle 

def flowerRecursion(t, n):
   if n > 0:
      #draw one petal
      t.forward(100)
      t.left(105)
      t.forward(52)
      t.left(105)
      t.forward(100)
      #prepare to move direction to draw next petal
      t.right(170)
      flowerRecursion(t, n - 1)

def main():
    t = turtle.Turtle()
    flowerRecursion(t, 9)

if __name__ == '__main__':
   main()