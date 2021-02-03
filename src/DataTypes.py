'''
Created on Nov 11, 2019

@author: 10644845
'''

'''**********************************Strings***************************************'''


str1 = 'Hello World!'

print (str1 )         # Prints complete string
print (str1[0])       # Prints first character of the string
print (str1[2:5])     # Prints characters starting from 3rd to 5th
print (str1[2:])      # Prints string starting from 3rd character
print (str1 * 2)      # Prints string two times
print (str1 + "TEST") # Prints concatenated string


'''**********************************Lists********************************************'''


list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']


print ("\n")  
print (list1)         # Prints complete list
print (list1[0])       # Prints first element of the list
print (list1[1:3])     # Prints elements starting from 2nd till 3rd 
print (list1[2:])    # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list1 + tinylist) # Prints concatenated lists


'''******************************Tuples***********************************************'''

tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print ("\n") 
print (tuple1)           # Prints complete list
print (tuple1[0])        # Prints first element of the list
print (tuple1[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple1[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple1 + tinytuple) # Prints concatenated lists


tuple2 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list2 = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
''' tuple2[2] = 1000    # Invalid syntax with tuple'''
list2[2] = 1000     # Valid syntax with list

'''*****************************Dictionaries*****************************************'''

dict1 = {}
dict1['one'] = "This is one"
dict1[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print ("\n") 
print (dict1['one'])      # Prints value for 'one' key
print (dict1[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values




