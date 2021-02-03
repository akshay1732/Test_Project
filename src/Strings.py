'''
Created on Nov 11, 2019

@author: 10644845
'''

var1 = 'Hello World!'
var2 = "Python Programming"


print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

print("\n")
print ("Updated String :- ", var1[:6] + 'Python')


print("\n")
print ("My name is %s and weight is %d kg!" % ('Zara', 21))

 

'''    *************    Triple Quotes    ***************************'''

para_str = """This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

print("\n")
print (para_str)

'''   *****************  Raw strings Displays as it is    ************'''
print("\n")
print ('C:\\nowhere')

print (r'C:\\nowhere')


'''    ******************      Functions   ****************************   '''



str1 = "this is string example....wow!!!"
print("\n")
print ("capitalize() : ", str1.capitalize())


'''Returns a string padded with fillchar with the original string 
centered to a total of width columns.'''

print ("str.center(40, 'a') : ", str1.center(40, 'a'))
str2='a'
print ("Count a : ", str1.count(str2,0,len(str1)))


str1 = "this2016"  # No space in this string
print("\n")
print (str1.isalnum())

str1 = "this is string example....wow!!!"
print (str1.isalnum())

str1 = "this";  # No space & digit in this string
print (str1.isalpha())

str1 = "this is string example....wow!!!"
print (str1.isalpha())


str1 = "This Is String Example...Wow!!!"
print (str1.istitle())

str1 = "This is string example....wow!!!"
print (str1.istitle())


'''    Join Elements in sequence    '''

s = " "
seq = ("a", "b", "c") # This is sequence of strings.
print("\n")
print (s.join( seq ))



'''        translation table '''

#replaces intab characters in outtab in string

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str1 = "this is string example....wow!!!"
print("\n")
print (str1.translate(trantab))


'''        spilt        '''

str1 = "this is string example....wow!!!"
print (str1.split( ))
print (str1.split('i',1))
print (str1.split('w'))







