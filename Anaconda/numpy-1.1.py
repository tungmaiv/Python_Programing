# http://nbviewer.jupyter.org/gist/manujeevanprakash/7e47301f0b50a98232ca
import numpy as np
scores = [89,56.34, 76,89, 98]
first_arr = np.array(scores)
print(first_arr)
print(first_arr.dtype)

scores_1 = [[34,56,23,89], [11,45,76,34]]
second_arr = np.array(scores_1)
print(second_arr)
print(second_arr.ndim)  #.ndim gives you the dimensions of an array.
print(second_arr.shape) #(number of rows, number of columns)
print(second_arr.dtype)

x = np.zeros(10)
print(x)
y = np.ones(10)
print(y)
z = np.zeros((4,5))
print(z)
n = np.arange(15)
print(n)
m = np.eye(7)
print(m)


