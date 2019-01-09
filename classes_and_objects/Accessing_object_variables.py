class MyClass:
    var = "bla"

    def function(self):
        print "This is a message inside the class."

myObjectX = MyClass() # FIRST OBJECT

myObjectX.var
print myObjectX.var

# we can create multiple different objects that have
# the same variables and functions defined

myObjectY = MyClass() # SECOND OBJECT
myObjectY.var = "pretty"

print myObjectY.var