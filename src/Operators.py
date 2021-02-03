'''
Created on Nov 11, 2019

@author: 10644845
'''


a = 21
b = 10
c = 0

'''       ***************  Arithmetic Operators   ******************  '''
c = a + b
print ("Line 1 - Value of c is ", c)

c = a - b
print ("Line 2 - Value of c is ", c) 

c = a * b
print ("Line 3 - Value of c is ", c) 

c = a / b
print ("Line 4 - Value of c is ", c) 

c = a % b
print ("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b 
print ("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b 
print ("Line 7 - Value of c is ", c)


'''    *******************    Comparison operators      ******************  '''
a,b,c = 21, 10,0

if ( a == b ):
    print ("\nLine 1 - a is equal to b")
else:
    print ("\nLine 1 - a is not equal to b")

if ( a != b ):
    print ("Line 2 - a is not equal to b")
else:
    print ("Line 2 - a is equal to b")
if ( a < b ):
    print ("Line 4 - a is less than b") 
else:
    print ("Line 4 - a is not less than b")
if ( a > b ):
    print ("Line 5 - a is greater than b")
else:
    print ("Line 5 - a is not greater than b")

a,b = 5,20;

if ( a <= b ):
    print ("Line 6 - a is either less than or equal to  b")
else:
    print ("Line 6 - a is neither less than nor equal to  b")

if ( b >= a ):
    print ("Line 7 - b is either greater than  or equal to b")
else:
    print ("Line 7 - b is neither greater than  nor equal to b")
    
    
'''        ***************    Assignment Operators     ******************** '''
    
c += a
print ("\nLine 2 - Value of c is ", c) 
c *= a
print ("Line 3 - Value of c is ", c)
c /= a 
print ("Line 4 - Value of c is ", c) 
c  = 2
c %= a
print ("Line 5 - Value of c is ", c)
c **= a
print ("Line 6 - Value of c is ", c)
c //= a
print ("Line 7 - Value of c is ", c)


'''        ********************    Bitwise Operators    *********************'''

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
c = a & b;        # 12 = 0000 1100
print ("\nLine 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)


'''        ***********************    Logical Operators    *******************'''
a=True; b=False;
c=a and b
print ("\nLine 1 - Value of c is ", c)

c=a or b
print ("Line 2 - Value of c is ", c)

c= not(a and b)
print ("Line 3 - Value of c is ", c)

'''       ***********************    Membership Operators    ******************'''

a = 10
b = 20
list1 = [1, 2, 3, 4, 5 ];

if ( a in list1 ):
    print ("\n a=10 is available in the given list")
else:
    print ("\na=10 is not available in the given list")

if ( b not in list1 ):
    print ("b=20 is not available in the given list")
else:
    print ("b=20 is available in the given list")

a = 2
if ( a in list1 ):
    print ("\na=2 is available in the given list")
else:
    print ("a=2 is not available in the given list")


'''        *******************    Ownership Operators    *********************'''
    
a = 20
b = 20

if ( a is b ):
    print ("\na and b have same identity")
else:
    print ("\na and b do not have same identity")

if ( id(a) == id(b) ):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")

b = 30
if ( a is b ):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")

if ( a is not b ):
    print ("a and b do not have same identity")
else:
    print ("a and b have same identity")