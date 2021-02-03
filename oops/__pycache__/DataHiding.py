'''
Created on 16-Nov-2019

@author: Akshay
'''

''''An object's attributes may or may not be visible outside the class definition.
 You need to name attributes with a double underscore prefix,
  and those attributes then will not be directly visible to outsiders.'''
  
  
class JustCounter:
    __secretCount = 0
  
    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter._JustCounter__secretCount)

try:
    print (counter.__secretCount)
    
except AttributeError:
    print("Cannot Access private attributes!")