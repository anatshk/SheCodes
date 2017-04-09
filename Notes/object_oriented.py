"""
Notes from lecture 11 - Object Oriented Programming (OOP)

a = 2  # creates an object of class 'int', with a label 'a', a unique id (uuid1), 'int' type and value of 2.
b = 3  # creates an object of class 'int', with a label 'b', a unique id (uuid2), 'int' type and value of 3.
c = 2  # labels an existing object (uuid1) with label 'c', to save space. this object now has 2 labels, 'a' and 'c'.

x = 4  # x is a name with a binding to an int object with value 2, this object has unique id (uuid3)
x = 5  # the name x is now bound to a DIFFERENT int object with value 5 and uuid4
# int is an immutable object, so the analogy of the "box with label x containing value 4" is incorrect.
# we cannot change the value of an 'int' object once its created, the assignment of existing name to a new value
# creates a new object. Unnamed objects (without bound names) are marked for garbage collection.
x = x + 1  # the value 5 is taken from the object labeled x, added to 1, we get the result 6.
# x is still immutable, so we cannot replace existing value 5 of the object labeled 'x' with the new value 6.
# a new int object is created, with the value 6, and the label 'x' is rebound to the new object (uuid5)

# Class - blueprint \ template for an object. Class has a name, what its like (attributes), what it can do (methods)
# Object attributes (properties?) - describing the object (for example, color)
# Object methods - functions that the object may perform.

class Name:
    blah = 'this is a class variable'  # all instances of the class have the same value

    def __init__(self, name='default name'):
        self.name = name  # this is an instance variable, each instance has its own value

    def say():
        print(self.name)

# class inheritance - base\super\parent class and sub\derived\child\heir class
# the child class inherits attributes and behavior from parent class

class Blerg(Name):  # class Blerg inherits from class Name
    def __init__(self):
        super().__init__()  # when initializing Blerg, call the constructor (ctor) of the parent\super class

# we can pass other variables to the init of the child class, overwriting the defaults of the super class
# and also add attributes and overwrite methods

class Blerg(Name):  # class Blerg inherits from class Name
    def __init__(self):
        super().__init__(name='default blerg', hair_color='brown')  # the default name is disserent from that of the parent class
        self.hair_color = hair_color  # additional attribute, does not exist in parent class

    def say():
        print(self.hair_color, self.name)  @ this method is overwritten - it is different from the parent


# Multiple Inheritance - inherit from 2 or more classes - getting all of their attributes and methods.
"""