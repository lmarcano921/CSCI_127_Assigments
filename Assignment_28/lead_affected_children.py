#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt
#Read in the csv file.
file = pd.read_csv('children_lead.csv')

#Group the data by location
option = input("Enter a choice \n a. group by borough \n b. group by year\n")

if(option == 'a'):
    groupAvg = file.groupby('borough')
    
    print("average number of affected children by borough")
    print("borough \n" + str(groupAvg['affected_children'].mean()))
    borough_input = input("Enter a borough: ")
    averageBorough = file.groupby('borough').get_group(borough_input)
    print("average number of affected children of " + borough_input + " is " + str(averageBorough['affected_children'].mean()))
    print("min number of affected children of " + borough_input + " is " + str(averageBorough['affected_children'].min()))
    print("max number of affected children of " + borough_input + " is " + str(averageBorough['affected_children'].max()))
elif(option == 'b'):
    groupAvg = file.groupby('year')
    
    print("average number of affected children by year")
    print("year \n" + str(groupAvg['affected_children'].mean()))
    year_input = input("Enter a year: ")
    averageYear = file.groupby('year').get_group(int(year_input))
    print("average number of affected children of " + year_input + " is " + str(averageYear['affected_children'].mean()))
    print("min number of affected children of " + year_input + " is " + str(averageYear['affected_children'].min()))
    print("max number of affected children of " + year_input + " is " + str(averageYear['affected_children'].max()))
else:
    exit("exiting")