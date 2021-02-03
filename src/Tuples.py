'''
Created on Nov 12, 2019

@author: 10644845
'''
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )

'''Any set of multiple objects with no enclosing Delimiters default to tuples'''
tup3 = "a", "b", "c", "d"

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("\ntup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])




tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;
tup3 = tup1 + tup2
print (tup3)


'''    deleting tuples   '''
tup = ('physics', 'chemistry', 1997, 2000);
print (tup)
del tup;



''' Passing list to tuple'''

list1 = ['maths', 'che', 'phy', 'bio']
tuple1 = tuple(list1)
print ("tuple elements : ", tuple1)
