import sys
import math
print(sys.executable)
print(sys.version)

print("\n")
x = 5
y = 119
z = 135.24
m = 100

print(math.exp(x))

print("math.exp(-45.17) : ", math.exp(-45.17))
print("math.exp(100.12) : ", math.exp(100.12))
print("math.exp(100.72) : ", math.exp(100.72))
# print("math.exp(119L) : ", math.exp(y))
print("math.exp(math.pi) : ", math.exp(math.pi))


print("\n")
print("abs(" + str(z) + ") = " + str(abs(z)))
print("fabs(" + str(z) + ") = " + str(math.fabs(z)))
print("math.ceil(" + str(z) + ") = " + str(math.ceil(z)))
print("math.floor(" + str(z) + ") = " + str(math.floor(m)))
print("math.log(" + str(100) + ") = " + str(math.log(m,)))
# print("cmp(" + str(x) + "," + str(y) + ") = " + str(cmp(x, y)))

print("\n")
var1 = 'Hello World!'
print("Updated String :- ", var1[:6] + "Python")

name = "tungvm"
age = 21
print("My name is %s and weight is %d kg!" % (name, age))
print("My name is {0} and weight is {1} kg!".format(name, age))
print("Good Bye!!!")
