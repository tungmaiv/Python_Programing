# 3d arrays -> this is a 2x2x3 array
import numpy as np 
three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(three_d_arr)
print("-----------------")
print(three_d_arr[0])
print("-----------------")
print(three_d_arr[0][1])
print("-----------------")
print(three_d_arr[0][1][1])

copied_values = three_d_arr[0].copy()
print("---------copy value---------")
print(copied_values)
copied_values[0][1] = 999
print("---------new copy value---------")
print(copied_values)
print("---------three dimentions array---------")
print(three_d_arr)