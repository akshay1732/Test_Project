'''
Created on Nov 11, 2019

@author: 10644845
'''


'''           ****************    IF Else **************************'''
  
var1 = 100
if var1:
    print ("1 - Got a true expression value", var1) 
else:
    print ("1 - Got a false expression value", var1) 
    
var2 = 0
if var2:
    print ("2 - Got a true expression value", var2)  
else:
    print ("2 - Got a false expression value", var2)
   
print ("Good bye!\n")

'''        ********************    loops     *********************'''


count = 0
while (count < 5):
    print ('The count is:', count)
    count = count + 1

print ("Good bye!\n")


for letter in 'Python':     # First Example
    print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
    print ('Current fruit :', fruit)
    
    
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print ('Current fruit :', fruits[index])
   

print ("Good bye!\n")



'''Using Else with loops'''

while count < 5:
    print (count, " is  less than 5")
    count = count + 1
else:
    print (count, " is not less than 5")
    
    

while (count<10): print ('Given flag is really true!');count = count + 1;
print ("Good bye!\n")
count = count + 1


for num in range(10,20):     #to iterate between 10 to 20
    for i in range(2,num):    #to iterate on the factors of the number
        
        if num%i == 0:         #to determine the first factor
            j=num/i            #to calculate the second factor
            pass
            print ('%d equals %d * %d' % (num,i,j))
            break #to move to the next number, the #first FOR
    else:  # else part of the loop
        print (num, "is a prime number")
   
    