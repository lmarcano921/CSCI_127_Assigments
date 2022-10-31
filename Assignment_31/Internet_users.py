#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

import pandas as pd

import matplotlib.pyplot as plt



file = pd.read_csv("country_internet.csv")
output = input("Enter output name: ")

file["Percentage"] = file["Internet users"]/file["Population"] * 100
file.plot(x = 'Country', y = 'Percentage')
print("maximum percentage of all countries:" , file["Country"].max() , file["Percentage"].max() , "%")
pop.plot(x = 'Country', y = 'Internet users')
fig = plt.gcf()
fig.savefig(output)