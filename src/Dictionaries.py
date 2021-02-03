'''
Created on Nov 12, 2019

@author: 10644845
'''
from Strings import seq

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict1['Name'])
print ("\ndict['Age']: ", dict1['Age'])

''' Adding and updating elements '''

dict1['Age'] = 8; # update existing entry
dict1['School'] = "DPS School" # Add new entry

print ("\ndict['Age']: ", dict1['Age'])
print ("\ndict['School']: ", dict1['School'])


'''Duplicate keys are not allowed'''

dict2 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("\ndict['Name']: ", dict2['Name'])


''' Functions '''

dict3 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
print ("\nEquivalent String : %s" % str (dict3))

seq = ('name', 'age', 'sex')

dict4 = dict.fromkeys(seq)
print("\n")
print (dict4)

dict5 = dict.fromkeys(seq, 10)
print (dict5)

'''return a tuple pairs'''
print ("Value : %s" %  dict3.items())

'''return a list of Keys'''
print ("Value : %s" %  dict3.keys())

'''    Update    '''
dict3.update(dict1)
print ("updated dict : ", dict3)