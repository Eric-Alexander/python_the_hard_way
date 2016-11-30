
#Notice a comma at the end of each raw_input indicates that a new line WILL NOT be added for user's answer-- it will appear on the same line as the question
print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",

weight = raw_input()

#remember when you are subbing in more than 1 format you must wrap the variables in paranthesis() and separate each variable with a comma
print "So, you're %r old, %r tall and weight %r pounds!" % (
age, height, weight)
#remember python programmers don't like using more than 80 characters per line
