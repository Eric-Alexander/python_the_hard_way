states = {
    'Washington': 'WA',
    'Arizona': 'AZ',
    'Oregon': 'OR',
    'New York': 'NY',
    'California': 'CA'
}

cities = {
    'WA': 'Seattle',
    'OR': 'Portland',
    'AZ': 'Flagstaff'
}

cities['NY'] = 'Rochester'
cities['CA'] = 'Los Angeles'

print '-' * 10
print "OR State has: ", cities['OR']

print '-' * 10
print "Washington's Abreviation is: ", states['Washington']
print "Washington has: ", cities[states['Washington']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated as %s" % (state, abbrev)
    
print '-' * 10
for abbrev, city in cities.items():
    print "%s State has %s as a city." % (abbrev, city)

print "+" * 20
for state, abbrev in states.items():
    print "%s state is abbreviated as %s and contains the city %s" % (state, abbrev, cities[abbrev])
