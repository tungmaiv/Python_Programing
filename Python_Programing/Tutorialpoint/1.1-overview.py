import sys
import random


print(sys.executable)
print(sys.version)

for i in range(5):
    print(random.random())

for num in [1, 2, 3, 4]:
    print(num)

a = b = c = 1
print(a)
print(b)
a = b + c
print(a)
print(b)
