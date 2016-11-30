print "I will now count my chickens:"

print "Hens", 25+30 / 6
print "Roosters", 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that is why it's false"

print "How about some more?"


print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2


cars = 100

space_in_a_car = 4.0
drivers = 30
passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "there are", cars, "cars available"
print "there are only", drivers, "drivers available"
print  "there will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have %s to carpool today" % passengers
print "We need to put about", average_passengers_per_car, "in each car."
