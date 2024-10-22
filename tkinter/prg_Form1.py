import numpy as np
# create a 1D array
array1 = np.array([1, 3, 5, 7, 9, 11])
# reshape the 1D array into a 2D array
array2 = np.reshape(array1, (2, 3))
# transpose the 2D array
array3 = np.transpose(array2)
print("Original array:\n", array1)
print("\nReshaped array:\n", array2)
print("\nTransposed array:\n", array3)

