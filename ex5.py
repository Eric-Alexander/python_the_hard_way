
#here I use the python formatter %d to substitute a piece of non-string data
#in this case it is the integer 10
x = "There are %d types of people." % 10
# I am setting the string "binary to a variable called binary"
binary = "binary"
#I am setting the string "don't to a variable called do_not"
do_not = "don't"
# I am setting a long string to the value of y with two string substitutions that
#I set prior
y = "THose who know %s and those who %s" % (binary, do_not)

print x

print y
# %r is a literal substitution. It will supplant, in this case, the entire quoted string of what ever was set to variable x with all subs (ie %d 10)
print "I said %r." % x
# this prints to console the value of the string, quotes omitted.
print "I also said: '%s'." % y
# I am setting a boolean of False to the variable hilarious
hilarious = False

# I am setting a string to the variable joke_evaluation with a %r formatter
joke_evaluation = "Isn't that joke so funny?! %r"
# this will print the string value of joke_evaluation and replace %r to the value of the variable hilarious, which, being a boolean, will be False
print joke_evaluation % hilarious

w = "This is the left side of ..."

e = "a string with a right side."

# By adding two variables together whose values are of the same data type, in this case a string, the + operator will concat the string values together
print w + e

#NOTe: in python one cannot concatonate to different data types
#Note: use %r for debugging and use %s, %d for displaying variables to others
g = "77"

h ='66'
print g+h
