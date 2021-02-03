'''
Created on 16-Nov-2019

@author: Akshay
'''
import os

"Create Directory"
print("Creating New Directory!")
os.mkdir("New Dir")

"Print Current Directory"
print("Current Working Directory:",os.getcwd())

"Change Directory"
os.chdir("New Dir")
print("After Changing Directory:",os.getcwd())
os.chdir("D:\EclipseWorkspace\PythonProject\src")
print("After Changing Directory:",os.getcwd())

"Remove Directory"
os.rmdir("New Dir")
print("New Dir Removed!")



"Files"
print("\nOpen New File!")
file =open("Input.txt","w+")
file.close()

print("Rename File!")
os.rename("Input.txt","Input1.txt")

print("Remove File!")
os.remove("Input1.txt")





