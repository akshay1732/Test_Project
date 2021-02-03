'''
Created on Nov 15, 2019

@author: 10644845
'''
from oops.Classes import Employee

class Child(Employee):
    def __init__(self):
        print("Child class Contructor:")
    def childMethod(self):
        print("Child Class Method")
        
    def myMethod(self):
        print ('Calling Child method')   
        
  
    
    
    
    
    
"Parent Class object"
p=Employee("Akshay", 5000)

"Child Class object"
c=Child()
c.name="AK"
c.salary="1000"


c.displayEmployee()
p.displayEmployee()
c.childMethod()
c.myMethod()
p.myMethod()





