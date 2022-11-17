#Luis A Marcano
#11/10/2022
#luis.marcano29@myhunter.cuny.edu

#Import the folium package for making maps
import folium
import pandas as pd

#Create a map, centered (0,0), and zoomed out a bit:

hospitals = pd.read_csv('nyc_hospitals.csv')
New_York_Map = folium.Map(location=[40.75, -74.125],zoom_start=10)

for index, row in hospitals.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Facility Name"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(New_York_Map)

#Save the map:
file = input("Enter output file: ")
New_York_Map.save(outfile=file)