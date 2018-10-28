import numpy as np 
matrix_arr = np.array([[3, 4, 5 ], [6, 7, 8], [9, 10, 11]])
print("The original matrix:\n{}".format(matrix_arr))
print("slices the first two rows:\n{}".format(matrix_arr[:2])) # similar to list slicing. returns first two rows of the array
print("Slices the first two rows and two columns:\n{}".format(matrix_arr[:2, :2]))
print("returns 6 and 7: \n{}".format(matrix_arr[1,:2]))
print("Returns first column:\n {}".format(matrix_arr[:,:1])) #Note that a colon by itself means to take the entire axis

from IPython.display import Image  # importing a image from my computer.
j = Image(filename='/Users/tungvm/Expre.png')
j # diagrammatic explanation of matrix array slicing works.

personals = np.array(['Manu', 'Jeevan', 'Prakash', 'Manu', 'Prakash', 'Jeevan', 'Prakash'])
print(personals == 'Manu')