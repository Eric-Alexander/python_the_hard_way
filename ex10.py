#the \t escape sequence provides a tabbed indent on the output
tabby_cat = "\tI'm tabbed in."
#the \n escape sequence provides a new line into the output
persian_cat = "I'm split\non a line."
# The \\ escape sequene provides a single backslash \ on the output

backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass

'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print u'\U0001F47E'

print "The world's own oyster \v lotty \v dotty \v joe \f WOO"


#this while displays a spinning binary NOTe: when the comma is removed on line 29 each item in the array gets printed on a new line
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i* 1000,

print "Hell\ro"
