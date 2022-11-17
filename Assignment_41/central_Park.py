#Luis A Marcano
#11/10/2022
#luis.marcano29@myhunter.cuny.edu
#coordinates 40.7812, -73.9665
#nyc_Central_Park.html

#Import the folium package for making maps
import folium

#Create a map, centered (0,0), and zoomed out a bit:
New_York = folium.Map(location=[40.75, -74.125],zoom_start=10)
folium.Marker(location = [40.7812, -73.9665], popup = "Central Park").add_to(New_York)
#Save the map:
New_York.save(outfile='nyc_Central_Park.html')