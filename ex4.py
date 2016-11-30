my_name = 'Eric A. Goetschel'
my_age = 27
my_heightin = 76.0
my_heightft = my_heightin / 12
my_weight = 208
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He is %d ft tall" % my_heightft
print "HE is %d pounds heavy" % my_weight
print "Actually that's not to heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % (my_teeth)

print "If I add %d, %d and %d I get %d." % (
my_age, my_heightft, my_weight, my_heightft + my_age + my_weight)

age = 6; fu = "bar"; string_literal = "This is a string"
print "Age: %d. String: %s. Literal: %r" % (age, fu, string_literal)


boo = "far away"

print boo.seek(1)
