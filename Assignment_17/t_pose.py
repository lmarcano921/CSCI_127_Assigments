#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/27/2022
#T-Shape assignment
import numpy as np
from PIL import Image

array = np.zeros([30, 30, 3], dtype=np.uint8)
array[:,:] = [255, 255, 0]   #yellow
array[5:8,5:25] = [0, 0, 255] #blue
array[8:25,13:16] = [0, 255, 0]   #green
img = Image.fromarray(array)
filename = input("Enter output file name: ")
img.save(filename)