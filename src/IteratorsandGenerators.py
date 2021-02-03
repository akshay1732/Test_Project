'''
Created on 16-Nov-2019

@author: Akshay
'''
import sys
def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while (counter <= n):
        yield a
        a, b = b, a + b
        counter += 1
        
            
f = fibonacci(5) #f is iterator object

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
            