import sys
import math
print(sys.executable)
print(sys.version)

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = ["a", "b", "c", "d"]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print("list2[:6]: ", list2[:6])
print("list2[7:]: ", list2[7:])

print("Value available at index 2 : ")
print(list1[2])
list1[2] = 2001
print("New value available at index 2 : ")
print(list1[2])

print("\n")
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)
list1.append(2015)
print(list1)

aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print("Extended List : ", aList)
