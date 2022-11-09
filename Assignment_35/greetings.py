#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

def whatHour(hour):

  if hour < 12:
    print("Good Morning")
  elif hour >= 12 and hour < 17:
    print("Good Afternoon")
  else:
    print("Good Evening")
h = int(input("Enter hour (in 24 hour time): "))

whatHour(h)