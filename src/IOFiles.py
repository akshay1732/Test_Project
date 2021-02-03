'''
Created on Nov 12, 2019

@author: 10644845
'''

x = input("Enter any Number:")
print("String Value:",x)
x=int(x)
z=x+10
print("Converted to int and Adding 10:",z)

x = input("\nEnter String:")
print("Entered String:",x) #entered data treated as string with or without ''

fileobj = open("Input.txt", "r+", 1)
print ("\nName of the file: ", fileobj.name)
print ("Closed : ", fileobj.closed)
print ("Opening mode : ", fileobj.mode)

'''*********************Reading strings from files*****************'''

fo = open("Input.txt", "r+")
str2 = fo.read(7)
print ("\nRead String is : ", str2)



'''*********************Writing from Files*************************'''

fileobj.write( "Python is a great language.\nYeah its great!!\n")




'''**********************File Position***************************** '''

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str2 = fo.read(10)
print ("Again read String is : ", str2)

# Close opened file
fo.close()


