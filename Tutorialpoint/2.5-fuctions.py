import sys

print(sys.executable)
print(sys.version)


def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


def changeme(mylist):
    "This changes a passed list into this function"
    mylist.append([1, 2, 3, 4])
    print("Values inside the function: ", mylist)
    return


# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print("Values of mylist the function: ", mylist)

mylist = [10, 20, 30]
print("Values of mylist outside the function: ", mylist)


def changeme1(mylist, i):
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4]  # This would assig new reference in mylist
    print("Values of mylist inside the function: ", mylist, i)
    i += 4
    return i


# error i is not defined
# print(i)
i = changeme1(mylist, 10)
print("Values of i outside the function: ", i)


# Function definition is here
def printinfo(name, age=20):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


# Now you can call printinfo function
printinfo(name="miki")
printinfo(age=50, name="miki")

# Function definition is here


def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50)

# Function definition is here


def sum(arg1, arg2): return arg1 + arg2


# Now you can call sum as a function
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))
