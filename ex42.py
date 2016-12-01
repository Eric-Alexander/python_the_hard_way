class Animal(object):
    pass

## class Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ##class Dog has-a attribute called name
        self.name = name
##class Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## class Cat has-a attribute called name
        self.name = name

##Class Person is-a object
class Person(object):
    def __init__(self, name):
        ##Person has-a attribute called name
        self.name = name
        ## Person has-a pet attribute with default set to None
        self.pet = None
##class Employee is-a Person aka E inherits from P
class Employee(Person):
    def __init__(self, name, salary):
        ##class Employee has-a attributes of self, name and salary
        ##this is a call to the parent, in this case, Person, and sets Person->Employee->name
        super(Employee, self).__init__(name)

        self.salary = salary
