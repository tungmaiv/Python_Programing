# Array indexing and slicing
import numpy as np 

new_arr = np.arange(17)
print(new_arr)
print(new_arr[5])
print(new_arr[4:9])
new_arr[4:9] = 99 #assign sequence of values from 4 to 9 as 99
print(new_arr)
# A major diffence between lists and array is that, array slices are views on the original array. This means that
# the data is not copied, and any modifications to the view will be reflected in the source
#  array. 
modi_arr = new_arr[4:9]
modi_arr[1] = 123456
print(new_arr)
print(modi_arr[:])
