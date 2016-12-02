class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override()"
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    ##Child is a sub class of Parent and, therefore, inherits attributes from Parent. They can be overwritten by defining a function by the same function name in the Parent class
    def override(self):
        print "CHILD override()"

    ##super is a way of calling for the execution of a function from a parent class. In this case it takes two arguments(Child, self) and calls the function altered() from theParent class
    def altered(self):
        print "CHILD before PARENT altered()"
        super(Child, self).altered()
        print "CHILD, after PARENT altered()"

dad = Parent()
son = Child()
fu = "+" * 20
dad.implicit()
son.implicit()
print fu
dad.override()
son.override()
print fu
dad.altered()
son.altered()
