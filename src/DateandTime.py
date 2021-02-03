"""
Created on Nov 12, 2019

@author: 10644845
"""
import calendar
import time;  # This is required to include time module.

ticks = time.time()
print("\nNumber of ticks since 12:00am, January 1, 1970:", ticks)

print(time.localtime());

'''convert seconds to time tuple'''

localtime = time.localtime(time.time())
print("\nLocal current time :", localtime)

'''    Getting formatted time  '''

localtime = time.asctime(time.localtime(time.time()))
print("\nFormatted time :", localtime)

'''Calender'''

cal = calendar.month(2016, 2)
print("\nHere is the calendar:\n")
print(cal)
