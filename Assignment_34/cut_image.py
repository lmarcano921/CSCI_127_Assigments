#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu
import matplotlib.pyplot as plt
import math

choice = int(input("Enter 1 to get upper right corner \nEnter 2 to get middle portion"))
print("Your choice:", choice)

if choice == 1:
    file = input("Enter input file name")
    img = plt.imread(file)
    outfile = input("Enter output file name")
    height = img.shape[0] #get height
    width = img.shape[1] #get width
    img2 = img[:height//2, width//2:]
    plt.imshow(img2)
    #plt.show()
    plt.imsave(outfile, img2)

elif choice == 2:
    file = input("Enter input file name")
    img = plt.imread(file)
    outfile = input("Enter output file name")
    height = img.shape[0]
    width = img.shape[1]

    img2 = img[height//4: math.floor(height-height//4), width//4:math.floor(width - width//4)]
    plt.imshow(img2)
    plt.show()
    plt.imsave(outfile, img2)
else:
    print("wrong choice")