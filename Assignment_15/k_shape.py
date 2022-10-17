#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/27/2022
#This program draws a brown triangle with 3 turtles

word = input("Enter a phrase: ")
list = word.split()
size = len(list)

for i in range(size,1,-1):   
     print(' '.join(list[:i]))

for i in range(1,size+1):   
     print(' '.join(list[:i]))