import numpy as np

arr = np.array([[-1, 5, -8],
                [9, 0, 2],
                [-6, 7, 3]])
# print(np.max(arr))  # return the maximum number from the given array
# print(arr.max())
# print(np.max(arr, axis=0))
# print(np.max(arr, axis=1))
# similarly same thing for " min "
# to print the index value  of " max or min element " in an array
# print(np.argmax(arr))
# print(np.argmax(arr, axis=0))
# print(np.argmax(arr, axis=1))
# print(np.argmin(arr))
# print(np.argmin(arr, axis=1))
# print(np.argmin(arr, axis=0))


# to change the element
# arr[2, 1] = 100
# print(arr)


# round off the value
arr1 = np.array([[-1.951, 5.545, -8.322],
                [9.3217, 0, 2.041],
                [-6.6651, 7.0867, 3.94]])
# print(np.around(arr1))
# print(np.around(arr1, decimals=2))  # after dot till two numbers
print(np.floor(arr1))
print(np.ceil(arr1))
