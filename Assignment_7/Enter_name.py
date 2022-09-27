#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 8/30/2022
#This program accepts user name then capitalizes the last name using the upper function
#Accept name from user in firstname lastname format sepparated by a space
fullName = input("Enter name in format firstName lastName: ")

#splits the string at the space character
fullName = fullName.split()

#Take advantage of the string index to re arrange the name in lastname, firstname format
print("name in LASTNAME, firstName format: " + fullName[1].upper() + ", " + fullName[0])

#Take email name from user and display it in hunter email format
username = input("Enter user name of email: ")
print("email: " + username.lower() + "@hunter.cuny.edu")