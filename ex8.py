formatter = "%r %r %r %r"
#note: when your are formatting more than one value you need to wrap them in
#patanthesis and separate each one by comma
print formatter % (1,2,3,4)


print formatter % ("one","two","three","four")


print formatter % (True, False, True, False)

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    "I had this thing.",
    "That you could type upright.",
    "But it didn't sing.",
    "So I said goodnight."
)

days =  "Mon Tues Wed Thurs Fri Sat Sun"
# \n represents a to start a New Line when printing out to the console
months = "Jan\nFed\nMar\nApr\nMay\nJune"

print  "Here are the days: ", days
print "Here are the months: ", months
# one can print entire comments that make automatic line breaks when
#hitting Enter---this assumes you have the Three " encasing the long comment
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
"""
