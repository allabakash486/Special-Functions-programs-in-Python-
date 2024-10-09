# Printng the squre of the numbers
def square(num):
    return num**2
print(list(map(square,[1,2,34,5,6,6,7,8])))
# USing lambda function it is too easy!.........
print(list(map(lambda a:a**2,[1,2,34,5,6,6,7,8])))
from functools import reduce
print(reduce(lambda a1,a2:a1*a2,range(1,6)))