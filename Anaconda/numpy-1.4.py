import numpy as np 
from IPython.display import Image # import image from computer
matrix_arr = np.array([[3, 4, 5], [6, 7, 8], [9, 5, 1]])
print(matrix_arr)
print(matrix_arr[1])
print(matrix_arr[0][2])
print(matrix_arr[0, 2])

i = Image(filename = "/Users/tungvm/mypict.png")
i