import numpy as np
from numpy import atleast_1d, where

# below all the arrays are created by numpy object 'np'
"""
arr = np.array([1, 2, 3, 4, 5, 6], np.int64)
print(arr)
print(arr[0])
print(arr.shape)  # (row,col)
print(arr.size)  # (length)
print(arr.ndim)  # (dimension)
print(arr.dtype)  # (datatype)
"""

"""
arr = np.array([[4, 69, 7, 54, 2]])
print(arr)
print(arr[0, 3])  # 2D array
print(arr.shape)  # (row,col)
print(arr.size)  # (length)
print(arr.ndim)
print(arr.dtype)
"""

"""
arr = np.array([[[4, 69, 7, 54, 2]]])
print(arr)
print(arr[0, 0, 3])  # 3D array
print(arr.shape)  # (row,col)
arr[0, 0, 3] = 45
print(arr[0, 0, 3])
print(arr.size)  # (length)
print(arr.ndim)
print(arr.dtype)
"""

"""
arr = np.array({1, 1, 2, 2})
print(arr)  # gives unique element
"""


# built-in array functions
# zeros = np.zeros((2, 5))  # 2D array
# print(zeros)

# rng = np.arange(15)
# print(rng)

# space = np.linspace(1, 50, 5)  # linearly spaced elements in such a way that we get 5 elements from 1-50
# print(space)                   # equally divides the number

# emt = np.empty([3, 3])  # create an array with random integers
# print(emt)

# identy = np.identity(5)  # identity matrix of 5x5
# print(identy)


"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# reshp = arr.reshape(3, 3)
reshp = np.reshape(arr, (3, 3))
print(reshp)
"""


# arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])  # change dimension of array into 1D
# changedim = np.ravel(arr)
# print(changedim)


#      AXIS
"""
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
# print(arr)
# print(arr.nbytes)
print(arr.sum(axis=0))
print(arr.sum(axis=1))
# print(arr.T)  # transpose of matrix
ar = arr.flat
for i in ar:
    print(i)
"""

"""
# gives the index of max & min number in an array
oneD = np.array([1, 32, 6, 64, 4, 2, 5])
print(oneD.argmax())
print(oneD.argmin())
"""


"""
# give the order of index value to sort elements
oneD = np.array([1, 32, 6, 64, 4, 2, ])
print(oneD.argsort())
"""

"""
arr = np.array([[9, 7, 8],
                [1, 2, 3],
                [6, 5, 4]])
# print(arr.argmax())
# print(arr.argmax(axis=0))  # y-axis
# print(arr.argmax(axis=1))  # x-axis
# print(arr.argmin())
# print(arr.argmin(axis=0))
# print(arr.argmin(axis=1))
print(arr.argsort())
print(arr.argsort(axis=0))  # y-axis
print(arr.argsort(axis=1))  # x-axis
"""

#     Matrix Operations
"""
arr1 = np.array([[9, 7, 8],
                [1, 2, 3],
                [6, 5, 4]])
arr2 = np.array([[9, 7, 8],
                [1, 2, 3],
                [6, 5, 4]])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)  # u cannot do same operations with lists
root = np.sqrt(arr1)
print(root)
print(arr2.sum())
print(arr2.max())
print(arr2.min())
"""

#     Searching elements
arr = np.array([[9, 7, 8],
                [1, 2, 3],
                [6, 5, 4]])
print(np.where(arr > 5, arr, arr*10))
print(np.where(arr > 5))  # it gives output base on the index of row & col
# print(np.where(atleast_1d(arr).nonzero()))
# print(np.count_nonzero(arr))
