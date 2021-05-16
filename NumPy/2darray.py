from numpy import *

array1 = array([
    [1, 2, 3],
    [4, 5, 6]
])

print(array1.ndim)
print(array1.shape)
print(array1.size)

# dimension convert

array2 = array1.flatten()
print("One dimension: ", array2)

array3 = array2.reshape(2, 3)
print("Two dimension: ", array3)

array4 = array2.reshape(1, 2, 3)
print("Three dimension: ", array4)
