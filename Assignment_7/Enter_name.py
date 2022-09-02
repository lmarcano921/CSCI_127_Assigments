#Name: Luis Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 8/30/2022
#This program accepts user name then capitalizes the last name using the upper function

#Accept name from user in firstname lastname format sepparated by a space
name = input("Enter name in format firstName lastName: ")

#splits the string at the space character
name = name.split(" ")

#Take advantage of the string index to re arrange the name in lastname, firstname format
print("name in LASTNAME, first name format: " + name[1].upper() + ", " + name[0])

#Take email name from user and display it in hunter enail format
email = input("Enter the user name of email: ")
print(email + "@myhunter.cuny.edu")