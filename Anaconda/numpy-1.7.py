# Fancy Indexing(Indexing using integer arrays)
import numpy as np 
from numpy import random


algebra = random.rand(7,4)
print (algebra)

for j in range(7):
    algebra[j] = j
print("------------------------------------------------")
print(algebra)
print("------------------------------------------------")
print(algebra[[1, 4, 5]])
print("------------------------------------------------")
fancy = np.arange(36).reshape(9,4)
print(fancy)
print("------------------------------------------------")
print(fancy[[1,4,3,2],[3,2,1,0]])
print("---select rows (1,4,8,2) and colums (0,3,1,2)---")
print(fancy[[1, 4, 8, 2]][:, [0, 3, 1, 2]])
print("---------------using numpy.ix_------------------")
print(fancy[np.ix_([1,4,8,2],[0,3,1,2])])