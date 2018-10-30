import sys
import math
import time
import calendar
print (sys.version)
print (sys.executable)
print("\n")

def printme(str):
    "This prints a passed string into this function."
    print (str)
    return
printme ("I'm first call to user defined function.")
printme ("Again call to the same function.")
print ("\n")
mylists = [1,2,3,4]
def changename(mylist):
    "This changes a past list into this function."
    mylist.extend(mylists)
    print ("Values inside the function:", mylist)
    return
mylist = [10,20,30,40]
changename (mylist)
print ("Values outside the function:", mylist)
print ("\n")

def changename(mylist):
    "This changes a past list into this function."
    mylist = [1,2,3,4]
    print ("Values inside the function:", mylist)
    return
mylist = [10,20,30,40]
changename (mylist)
print ("Values outside the function:", mylist)
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;
printme( str = "My string")
print ("\n")
def printinfo (name , age = 35):
    "This prints the info a passed info into this function."
    print ("Name:", name)
    print ("Name:", age)
printinfo (age = 15, name = "Jeff")
printinfo (name = "Dave")
print ("\n")
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
printinfo( 10 )
printinfo( 70, 60, 50 )
print ("\n")
sum = lambda arg1, arg2: arg1 + arg2;


print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
def sum( arg1, arg2 ):
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;
total = sum( 10, 20 );
print ("Outside the function : ", total)
def sum( arg1, arg2 ):
   total = arg1 + arg2;
   print ("Inside the function local total : ", total)
   return total;
sum( 10, 20 );
print ("Outside the function global total : ", total) 
