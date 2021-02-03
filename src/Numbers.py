'''
Created on Nov 11, 2019

@author: 10644845
'''
import math 
from pip._vendor.pytoml.writer import long
from math import ceil, pi
import  random
from random import choice, randrange, uniform, shuffle

a=int(15.9)
print(a)

b=float(45)
print(b)

c=long(2)
print(c)

d=complex(45,2)
print(d)


a=-10.823
print("\n")
print(abs(a))
print(math.fabs(a))
print(ceil(a))
print(math.floor(a))
print(math.modf(a))
print(round(a, 1))

'''        *********************Random Number Functions    ********************'''

print("\n")
list1=[1, 2, 3, 5, 9]
print(choice(list1))
print(shuffle(list1))
print(random.choice(range(100)))
print(randrange(0,10,2))
print(uniform(1,2))
print(random.random())


random.seed()
print ("\nrandom number with default seed", random.random())

random.seed(10)
print ("random number with int seed", random.random())

random.seed("hello",2)
print ("random number with string seed", random.random())
print(pi)