#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/27/2022
#This program draws a brown triangle with 3 turtles

import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('csBridge.png')   #Read in image from csBridge.png
img[:,:,0] = 0          #Set the RED channel to 0
plt.imsave('csBridge_wo_red.png', img)  #Save the image we created to the file: reds.png
img2 = plt.imread('shadesOfPurple.png')   #Read in image from csBridge.png
img2[:,:,0] = 0          #Set the RED channel to 0
plt.imsave('shadesOfPurple_wo_red.png', img2)  #Save the image we created to the file: reds.png