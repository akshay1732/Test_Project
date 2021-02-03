'''
Created on Nov 12, 2019

@author: 10644845
'''



# Function definition is here
def printme( str1 ):
    "This prints a passed string into this function"
    print (str1)
    return

# Now you can call printme function
printme("This is first call to function!")
printme("Again second call to the same function!")




def changeme( mylist ):
    "This changes a passed list into this function"
    print ("\nValues before change: ", mylist)
   
    mylist[1]=50
    print ("Values after change: ", mylist)
   
    mylist = [1,2,3,4] # This would assign new reference in mylist
    print ("Values after change2: ", mylist)
    return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

'''calling a Function '''



'''1.*********** Required Arguments *******************'''

def printme1( str2,num=10):
    "This prints a passed string into this function"
    print("\n")
    print (str2,num)
    return
# Now you can call printme function
#order is important

printme1("Argumentone",3)



'''2. ************* Keyword Arguments ******************'''
#using same argument names order is not required

printme1(num=3,str2="Argumentone")



'''3. *************    Default Arguments *************** '''
printme1("Argumentone") #will print default value of num 10


'''4. Variable Arguments '''

def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("\nOutput is: ")
    print (arg1)
   
    for var in vartuple:
        print (var)
    return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )



'''******************* Anonymous Functions ***************************** '''
sum1 = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print ("\nValue:", sum1( 10, 20 ))
print ("Value:", sum1( 20, 20 ))


