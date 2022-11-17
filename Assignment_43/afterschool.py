#Luis A Marcano
#11/10/2022
#luis.marcano29@myhunter.cuny.edu

#Import the folium package for making maps
import folium
import pandas as pd
import re

schools = pd.read_csv('after_school.csv')
New_York_Map = folium.Map(location=[40.75, -74.125],zoom_start=10)
choice = int(input("Enter 1 for Borough/Community,\n2 for Grade Level / Age Group"))

if(choice == 1):
    print("Your choice: ", choice, "\ndict_keys(['Astoria', 'Bronx', 'Brooklyn', 'Corona', 'Flushing',",
        "'Forest Hills', 'Jackson Heights', 'Jamaica', 'Kew Gardens', 'Long Island City', 'Manhattan',",
        "'New York', 'Queens', 'Staten Island', 'Woodside'])")
    borough = input("Enter Borough/Community name: ")
    grouped = schools.groupby('Borough/Community').get_group(borough)
    
    for index, grouped in grouped.iterrows():
        lat = grouped["Latitude"]
        lon = grouped["Longitude"]
        name = grouped["Name"]
        newMarker = folium.Marker([lat, lon], popup=name)
        newMarker.add_to(New_York_Map)
        
    newborough=""
    borough = borough.lower()
    borough = re.split( " |,|/", borough)
    
    for i in range(len(borough)):
        borough[i] +="_"
        newborough += borough[i]
  
    newborough += "after_school.html"
    New_York_Map.save(outfile= newborough)

elif(choice == 2):
    print("Your choice: ", choice)
    grade = input("Enter Grade Level / Age Group: ")
    grouped = schools.groupby('Grade Level / Age Group').get_group(grade)
   
    for index, grouped in grouped.iterrows():
        lat = grouped["Latitude"]
        lon = grouped["Longitude"]
        name = grouped["Name"]
        newMarker = folium.Marker([lat, lon], popup=name)
        newMarker.add_to(New_York_Map)
        
    grade = grade.lower()
    grade = re.split( " |,|/", grade)
    newgrade = ""
    
    for i in range(len(grade)):
        grade[i] +="_"
        newgrade += grade[i]
        
    newgrade += "after_school.html"
    New_York_Map.save(outfile= newgrade)

    
elif (choice == 3):
    grade = input("Enter Grade Level / Age Group: ")
    grade = grade.lower()
    grade = re.split( " |,|/", grade)
    newgrade = ""
    for i in range(len(grade)):
        grade[i] +="_"
        newgrade += grade[i]
        print(newgrade)
    
    print(newgrade)
    """
    grade = grade[len(grade)- 2]
    grade += "_after_school.html"
    print(grade)
    """
else:
    print(["Error"])
