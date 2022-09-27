#Name: Luis A Marcano
#Email: luis.marcano29@myhunter.cuny.edu
#Date: 9/22/2022
#This program takes a phrase, reverses the phrase then capitalizes the reverse string


reverse = " "
upper_string= " "
abv = " "

phrase = input("input: ")
for i in reversed(phrase):
    reverse += i
upper_string = reverse.upper()
rev_string = reverse.split()

print("user reverse: " + reverse)
print("user reverse upper: " + upper_string)
print("user abbreviation: ", end = "")

for i in range(len(rev_string) - 1, -1, -1):
    print(rev_string[i][-1].upper(), end ="")