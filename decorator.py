def myDecorator(function):

    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print("I am decorating your function")

    return wrapper

@myDecorator
def hello_world():
    print("Hello World!")

@myDecorator
def hello_person(person):
    print(f"Hello {person} !")

#hello_world()
hello_person('Sourabh')

###
#Example Logging
###

def logged(function):

    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value} \n")
        return value
    return wrapper

@logged
def add(x,y):
    return x+y

print(add(10, 20))


###
# Second example
###

import time

def timed(function):
    def wrapper(*args, **kwargs):
        before  = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute")
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

myfunction(90000)