# create a seq without using lists
import sys

def mygen(n):
    for x in range(1, n):
        yield x ** 3
    
values = mygen(9000)

for each in values:
    print(each)
print(sys.getsizeof(values))

###
# Creating an infinite sequence without storing any values
###

def infi_seq():
    res = 1
    while True:
        yield res
        res *= 5

values = infi_seq()

print(next(values))
print(next(values))
print(next(values))