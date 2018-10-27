import sys
import math
print (sys.version)
print (sys.executable)

z = 10
m = 130.12

print (int(3.14))
print (float(100))
print (complex(10.456))
print (complex(10.9,2.34))

print(math.exp(1))

print("math.exp(-45.17) : ", math.exp(-45.17))
print("math.exp(100.12) : ", math.exp(100.12))
print("math.exp(100.72) : ", math.exp(100.72))
print("math.exp(math.pi) : ", math.exp(math.pi))

print("\n")
print("abs(" + str(z) + ") = " + str(abs(z)))
print("fabs(" + str(z) + ") = " + str(math.fabs(z)))
print("math.ceil(" + str(z) + ") = " + str(math.ceil(z)))
print("math.floor(" + str(z) + ") = " + str(math.floor(m)))
print("math.log( ," str(100) + ") = " str(math.log(m,)",)

name = "Jeff"
weight = 68
print("My name is %s and weight is %d kg!" % (name, weight))
print("My name is {0} and weight is {1} kg!".format(name, weight))
