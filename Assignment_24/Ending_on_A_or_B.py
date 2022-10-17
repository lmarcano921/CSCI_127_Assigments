#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu
#Detect ending in a or b

words = input("Enter a list of words, separated by a space: ")
words = words.split()
numWords = numAorB = fraction = 0

for i in words:
     numWords += 1
     if i[len(i)-1] == 'a' or i[len(i)-1] == 'b':
          numAorB += 1

fraction = numAorB/numWords
print("number of words: " + str(numWords))
print("number of words ending with a or b: " + str(numAorB))
print("fraction of words ending with a or b: " + str(fraction))