#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("country_internet.csv")

grouped_data = file.groupby('Continental region')
print(grouped_data["NO. OF Internet Plans"].mean())
print("possible regions are ", "dict_keys(['ASIA (EX. NEAR EAST)', 'BALTICS', 'CARIBBEAN', 'CENTRAL AMERICA', 'CIS (FORMER USSR)', 'EASTERN EUROPE', 'Europe', 'NEAR EAST', 'NORTHERN AFRICA', 'NORTHERN AMERICA', 'OCEANIA', 'SOUTH AMERICA', 'SUB-SAHARAN AFRICA', 'WESTERN EUROPE'])")
region = input("choose a region")
gc = file.groupby('Continental region').get_group(region)
print ("In region" , region, 
       "\nnumber of countries", int(gc['Continental region'].value_counts()),
       "\nmaximum number of internet plans:", gc['NO. OF Internet Plans'].max(),
       "\nminimum number of internet plans:", gc['NO. OF Internet Plans'].min())

output = input("Please enter output file name:")


grouped_data.get_group(region).plot.bar(x='Country', y='NO. OF Internet Plans')
plt.gcf().subplots_adjust(bottom=0.25)
plt.xlabel("Country in NORTHERN AMERICA")
plt.ylabel("NO. OF Internet Plans")

fig = plt.gcf()
fig.savefig(output)