'''
Created on Nov 15, 2019

@author: 10644845
'''



"Exception Handling"

try:
    a= input("Enter Even Number:")
    b=int(a)%2
    assert (b==0)
    
    b=input("Enter Filename to Read:")
    fh = open(b, "r+")
    print("Writing in file!")
    fh.write("This is my test file for exception handling!!")
    
except IOError as Argument:
    print ("Error: can\'t find file or read data!")
    print(Argument)
except AssertionError :
    print ("Error: Not an Even Number!")
    
else:
    print ("Else block - No Expection Occured")
    fh.close()
finally:
    print("Finally block\n")    

try:
    c= int("10")
except ValueError as Argument:
    print ("\nThe argument does not contain numbers\n", Argument)
    
    
"Raising Exceptions"

def functionName( level ):
    if level <1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception    
        return level

try:
    l = functionName(-10)
    print ("level = ",l)
except Exception as e:
    print ("Error in level argument",e.args[0])
    
    
"User defined Exceptions"

class Myerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
    def __str__(self): 
        return(repr(self.arg)) 
try:
    raise (Myerror("Bad hostname"))
except Myerror as error:
    print (error.arg)







