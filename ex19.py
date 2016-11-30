def cheese_and_crackers(cheese_count, crackers_count):
    print "You have %d cheeses" % cheese_count
    print "Tou have %d boxes of crackers!!!FUCK YEAH" % crackers_count
    print "It's fuckin party timE!"
    print "Get a blanket. \n"


print "We can just give the function numbers directly:"
cheese_and_crackers(66,22)

print "OR, we can use variables from our script:"
amount_cheese = 50
amount_crackers = 30

cheese_and_crackers(amount_cheese, amount_crackers)

print "We can do math inside the arguemnets as well:"
cheese_and_crackers(1+1+1+1, 666-1)

print "And we can combine both variables and math like so:"
cheese_and_crackers(amount_cheese + 4, amount_crackers - 2)
