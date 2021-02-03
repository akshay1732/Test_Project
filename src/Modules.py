'''
Created on Nov 12, 2019

@author: 10644845
'''
# Import built-in module math
import math


# Executing Modules as Scripts

def fib(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    f = fib(100)
    print(f)


content = dir(math)

print(content)

# for var in content:
#     print (var)

