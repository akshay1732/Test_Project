'''
Created on Nov 12, 2019

@author: 10644845
'''
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


'''    ***************    Updating Lists    *********************'''

print ("\nValue available at index 2 : ", list1[2])

list1[2] = 2001
print ("New value available at index 2 : ", list1[2])


''' **********************  Deleting Values  ******************************'''

print("\n")
print (list1)

del list1[2]
print ("\nAfter deleting value at index 2 :", list1)


'''******************* Indexing, Slicing and Matrixes   ********************'''


L = ['C++','Java','VBScript','Python']
L1=['Selenium','UFT','HP']

T = ('Selenium','UFT','HP')
print("\n")
print(L[1])
print(L[-1]) #count from right
print(L[1:])

print(max(L))
print(list(T)) #convert tuples into lists

L.append(L1)
print(L)
L = ['C++','Java','VBScript','Python']
L.extend(L1)


print(L)

