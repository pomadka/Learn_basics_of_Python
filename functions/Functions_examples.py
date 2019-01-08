def my_function_1():
    hello_peaople()
    print ("Function 1!")


def hello_peaople(name):
    print ("hello %s" % name)
hello_peaople("Vlada")


def sum(a, b):
    print ("sum ias called!")
    return a + b


sumOfNums = sum(sum(1, 4), 5)
print sumOfNums

def my_function():
    print("Hello From My Function!")
my_function() # prints out "Hello from my function"