#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/27/2022
#This program joins a list of names

word = input("Enter a list of names separated by a ;")
word = word.split(";")

for i in word:
     print (i[0].upper() + ". " + i.split()[1])