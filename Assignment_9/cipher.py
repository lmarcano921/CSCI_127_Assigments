#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/17/2022
#This program takes a phrase then shifts the string by 13 letters making it a coded message

message = input("Enter an all-small-letter string: ")
cipher = int(input("Enter a non-negative int to shift: "))
new_message = ""

for i in range(len(message)):
    char = message[i]
    new_message += chr((ord(char) + cipher - 97) % 26 + 97)
print("ciphered string: " + new_message)

