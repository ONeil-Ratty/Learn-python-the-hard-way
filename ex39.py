# create a mapping or state to abbreviation

states = {
    "Oregon" : "OR",
    "Florida" : "FL",
    "California" : "CA",
    "New York" : "NY",
    "Michigan" : "MI",
}

# create a basic set of states and some cities in them

cities = {
    "CA" : "San Francisco",
    "MI" : "Detroit",
    "FL" : "Jacksonville",
}

# adding some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print('-' * 10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ",states["Michigan"])
print("Florida's abbreviation is: ",states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ",cities[states["Florida"]])

# print every statae abbreviation
print('-' * 10)
for state,abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for state, city in cities.items():
    print(f"this is the {state} and the {city} inside in it.")

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print(f"this is the {state} and the {city} and has the city {cities[abbrev]}")


print("-" * 10)
# safetly get an abbreviation by state that might not be there
state = states.get("Texas",None)

if not state:
    print("Sorry, not Texas.")

# get a city with a default value
city = cities.get('TX','Does Not Exist')
print(f"The city for the same state 'TX' is: {city}")
