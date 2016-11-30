from sys import argv
# after importing the arguments from the system module we declare the script(this module)
#and the fiename we want to read as arguements
script, filename = argv

# I am setting the variable txt to the built-in python method open() in which takes a value of a file name. An optional second argument is HOW the file is to be opened.
#For example, putting 'r' as the second arguement will READ-ONLY the file in this case use 'r' as a second arguement is redundant
txt = open(filename)

print "Here's your file %r:" % filename

print txt.read()

# print "Type rhe filename again:"
#
# file_again = raw_input("> ")
#
# txt_again = open(file_again)
#
# print txt_again.read()

txt.close()

# txt_again.close()
