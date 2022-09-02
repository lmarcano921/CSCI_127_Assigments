#Name: Luis Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 8/30/2022
#This program takes a phrase then prints the character and its ASCII code

phrase = input("Enter a phrase: ")
nexttwo = 2
for i in phrase:
    print (phrase[i] + " " + ord[i] + " " + phrase[nexttwo])
    nexttwo+=2
    