def add(a,b):
    print "addddding %d + %d" % (a,b)
    return a + b
fu = add(6,5)

def subtract(a, b):
    print "subtracting %d - %d" % (a,b)
    return a - b

def multiply(a, b):
    print "multiplying %d * %d" % (a,b)
    return a * b

def divide(a,b):
    print "dividing %d / %d" % (a,b)
    return a / b

print "Let's do something fun with functions"

age = add(20, 7)
height = subtract( 74, 2)
weight = multiply(100, 2)
iq = divide(300, 4)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "can you do it by hand?"
