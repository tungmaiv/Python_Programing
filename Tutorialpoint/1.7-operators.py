import sys
print(sys.executable)
print(sys.version)

a = 20
b = 10

print("\n")
print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

a = 21
print("\n")
print(a % b)
print(a // b)
a = -20
print(a // b)
a = 10
b += a
print(b)
c = d = 1
e = 1
f = 1.0
# b = 0x00001101

print(c is d)
print(c is e)
print(c == f)
print(c is f)

c += 1
print(c is d)
