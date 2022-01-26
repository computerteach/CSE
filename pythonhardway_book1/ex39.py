#create a mapping state abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

#create a basic set of states and some cities in them
cities ={
    'CA' : 'San Francisco',
    'MI' :  ' Detroit', 
    'FL' : 'Jacksonville'
}

#add some more cities
cities ['NY'] ='New York'
cities ['OR'] ='Portland'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print( "Florida's abbreviation is:", states['Florida'])

#do it using the state then the  cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has; ", cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev, in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
   
#print every city in the state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f" and has city{cities[abbrev]}")

print('-' * 10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("sorry, no Texas.")

#get a city with a default value
city = cities.get('TX', 'Does  not exist')
print(f"The city for the state 'TX' is {city}")


things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] ='z'
print (things [1])

things
['a', 'z', 'c', 'd']

