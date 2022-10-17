#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 10/10/2022
#This program draws stripes in alternating colors

import numpy as np
import matplotlib.pyplot as plt

lines = int(input("Enter the size"))
array = np.zeros((lines, lines, 3))


array[:,0::2,2] = 1.0 #set to blue
array[:,1::2,1] = 1.0 #set green to 1

plt.imshow(array)
plt.show()
filename = input("Enter output file name: ")
plt.imsave(filename, array)