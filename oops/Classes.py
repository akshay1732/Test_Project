'''
Created on Nov 15, 2019

@author: 10644845
'''
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)
        
    def myMethod(self): 
        print ('Calling parent method')
    
    
        
        
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)  


emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employees: %d" % Employee.empCount)


emp1.salary = 7000  # Add an 'salary' attribute.
emp1.name = 'Nora'  # Modify 'name' attribute.
emp1.displayEmployee()




"Attributes functions"

print(hasattr(emp1, 'salary'))    # Returns true if 'salary' attribute exists
print(getattr(emp1, 'salary'))    # Returns value of 'salary' attribute
setattr(emp1, 'salary', 6000) # Set attribute 'salary' at 7000
delattr(emp1, 'salary')    # Delete attribute 'salary'
print(hasattr(emp1, 'salary')) 



"Built-In Class Attributes"

print ("\nEmployee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )



