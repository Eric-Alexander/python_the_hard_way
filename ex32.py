the_count = [1,2,3,4,5]

fruits = ['apples', 'oranges', 'pears', 'apricots']

change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit


for i in change:
    print "I got %r" % i

elements = []
#this is a common way to write a finite for-loop in Python in which range(arg1, arg2) takes two arguments. The first being the start index and the second being up-to-but-not-including the integer specified.
for i in range(0,6):
    print "Adding %d to the list." % i
    elements.append(i)

for i in elements:
    print "Element was: %d" % i
