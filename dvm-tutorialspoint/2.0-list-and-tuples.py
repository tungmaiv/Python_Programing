import sys
import math
print (sys.version)
print (sys.executable)

list1 = ["math", "physics" , "biology" , "programming" ]
list2 = [1, 2, 3, 4, 5, 6, 7]
print ("First subject of the day :", list1[0])
print ("The numbers are : ", list2[3:5] )
print ("\n")
list = [23,5,66,334,693]
print ("Value at index 4:")
print (list[4])
list[4] = 600
print ("New value at index 4:")
print (list[4])
print ("\n")
list3 = ["Invictus Gaming","G2 Esports","Cloud9","Fnatic"]
print ("The semifinalists of Worlds are :",list3)
del list3[1]
print ("UPDATE! G2 esports have just been knocked out so the only teams left are: ",list3,"left")
print ("\n")
print (len(list2))
print (max(list2))
print (min(list2))
list2.extend(list1)
print (list2)
list.reverse()
print (list)
print ("DONE.")
