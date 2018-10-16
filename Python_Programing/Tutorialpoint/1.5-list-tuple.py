import sys
print(sys.executable)
print(sys.version)

tuple = ('abcd', 786, 2.23, 'john', 70.2)
list = ['abcd', 786, 2.23, 'john', 70.2]


print("\n")
print(list[2])
# tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list
print("\n")
print(list[2])

mylist = [10, 20, 30]
i = 3
i = changeme1(mylist, i)
print("Values outside the function: ", mylist, i)

courses = ["History", "Math", "Further Math"]
ext_courses = ["Physics", "Biology"]
courses.insert(0, ext_courses)
print(courses[0][0])
