#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

import pandas as pd

file = pd.read_csv("movie_locations.csv")

neighborhooods = int(input("order of most popular neighborhoods in movies: "))
print(file["Neighborhood"].value_counts()[:neighborhooods])

directors = int(input("order of directors/filmmakers making most movies in NYC: "))
print(file["Director/Filmmaker Name"].value_counts()[:directors])