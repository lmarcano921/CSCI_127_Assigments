#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu
#Count white pixels

import matplotlib.pyplot as plt

file = input("Enter file name: ")
t = float(input("Enter threshold: "))
ca = plt.imread(file)   #Read in image
countSnow = 0            #Number of pixels that are almost white
pixelSum = 0 
#For every pixel:

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        #Check if red, green, and blue are > t:

        if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
            countSnow = countSnow + 1
        pixelSum += 1

percent = round(((countSnow/pixelSum)*100),2)
print("number of white pixels: " + str(countSnow))
print("percent of white pixels: " + str(percent) + " %")