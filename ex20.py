from sys import argv

script, input_file = argv
# this function takes ina single parameter and uses the built-in Pyhton function read() to skim thru the file. It does not output to console.
def print_all(f):
    print f.read()
#this function takes a single paramter and uses the file.seek() to locate a given line. In this case 0 pertains to first character or byte in the line.
def rewind(f):
    f.seek(0)
#file.readline() will print/read a line, byte by byte, all the way until it hits a \n format. Then, it reports what it has found so far up until that point.
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a VHS tape yayyyuhhhhh"

rewind(current_file)

print "Now we shall print three lines: \n"

current_line = 1
#we are setting the FIRST line of the selected File
print_a_line(current_line, current_file)

current_line += 1
#this would be the SECOND line
print_a_line(current_line, current_file)

current_line =+ 1
#THIS WOULD BE THIRD LINE
print_a_line(current_line, current_file)
