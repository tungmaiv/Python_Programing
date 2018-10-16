import sys

print(sys.executable)
print(sys.version)

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0  1  2  3  4  5  6  7  8  9
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print("\n")
print(list)              # Prints complete list
print(list[0])           # Prints first element of the list
print(list[1:3])         # Prints elements starting from 2nd till 3rd
print(list[2:])          # Prints elements starting from 3rd element
print(tinylist * 2)      # Prints list two times
print(list + tinylist)  # Prints concatenated lists

print(my_list[1::2])
print(my_list[-1:1:-2])

mylist = [10, 20, 30]
i = 3
# i = changeme1(mylist, i)
print("Values outside the function: ", mylist, i)

courses = ["History", "Math", "Further Math"]
ext_courses = ["Physics", "Biology"]
courses.insert(0, ext_courses)
print(courses[0][0])
