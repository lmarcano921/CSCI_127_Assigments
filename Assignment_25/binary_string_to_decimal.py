#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

binary_string = input("Enter a binary number as 0 and 1")
num = 0
base = 2
weight = 1
binary_length = len(binary_string)
 
for ch in range(binary_length-1,-1, -1):
    if binary_string[ch] == '1':
        num += weight
    elif binary_string[ch] != '0':
        print ("Letter " + str(binary_string[ch]) + " is not allowed in a binary string.")
        exit()
    weight *= base
        
print("num = " + str(num))