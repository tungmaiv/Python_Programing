# Universal functions
import numpy as np 

funky = np.arange(17)
print(funky)
print("---------------numpy.sqrt--------------")
print(np.sqrt(funky))
print("---------------numpy.exp--------------")
print(np.exp(funky))
print("______________________________________")
x = np.random.rand (10)
y = np.random.rand (10)
print(x)
print(y)
print(np.maximum(x,y))
print(np.modf(x))