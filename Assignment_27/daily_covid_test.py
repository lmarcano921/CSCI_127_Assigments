#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu
#this program takes a csv, and uses user input to display borough covid data

import pandas as pd
import matplotlib.pyplot as plt
#Read in the csv file.
file = input("Enter a csv file: ")
file = pd.read_csv(file)

#Group the data by location
borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
output = input("Enter output name: ")

print("Min: " + str(round(file[borough].min(),3)))
print("Max: " + str(round(file[borough].max(),3)))
print("Mean: " + str(round(file[borough].mean(),3)))
print("Median: " + str(round(file[borough].median(),3)))
print("Standard Deviation: " + str(round(file[borough].std(),3)))
file["Fraction"] = file[borough]/file["case_count"]
file.plot(x = 'date_of_interest', y = 'Fraction')
fig = plt.gcf()
fig.savefig(output)