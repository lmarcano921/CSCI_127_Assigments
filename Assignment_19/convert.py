#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 10/10/2022
#This program converts centimeters to feet
#convert cm to feet
#convert cm to feet and inches

import numpy as np

selection = input("(a) convert centimeters to feet (b) convert centimeters to feet and inches (c) convert feet and inches to centimeters. \n\"Enter a or b or c: \")")

if (selection == 'a'):
    cm = int(input("Enter height in centimeters: "))
    print("height is " + str(round(cm / 30.48,2)) + " feet")
    
elif(selection == 'b'):
    num = int(input("Enter height in centimeters: "))

    num /= 30.48

    dec = int((num % 1)12)

    height = int(num)

    if dec == 0:

        print("height is " + str(height) + " feet")

    else:

        print("height is " + str(height) + " feet and " + str(dec) + " inches")
elif(selection == 'c'):
    feet_str, inches_str = input("Enter height in feet and inches, separated by a space: ").split()
    #convert feet_str to an int using 
    feet = float(feet_str) * 30.48
    inches = float(inches_str) * 2.54
    cm = feet + inches
    print("height is " + str(round(int(cm))) + " centimeters")

else:
    print("Wrong choice, please enter only a or b or c.")