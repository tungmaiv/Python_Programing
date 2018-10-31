
# Transposing Arrays
import numpy as np 
transpose = np.arange(12).reshape(3, 4)
print(transpose)
print("------------shape change to 4,3--------")
print(transpose.T)
print("------------using np.dot--------")
print(np.dot(transpose.T, transpose))

