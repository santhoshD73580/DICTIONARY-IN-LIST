country = input("Enter the name of country: ") # Add country name
visits = int(input("How maney times do you visited: ")) # Number of visits
list_of_cities = eval(input("List the cities on it: ")) # create list from formatted string
# Brazil
# 2
# ["Sao Paulo", "Rio de Janeiro"]

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, visited, cities):
  """task to add new countery in the travel vlog"""
  new_countries ={}
  new_countries["country"]= name
  new_countries["visits"]= visited
  new_countries["cities"] = cities
  travel_log.append(new_countries)#append
  
  


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")