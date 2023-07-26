import numpy as np

arr1 = np.array([[4, 5, 7, 3, 2], [9, 4, 3, 1, 5]])
arr2 = np.array([[8, 15, 7, 3, 4], [90, 31, 11, 6, 52]])

# " S t a c k i n g "  joining the one array with another in vertical or horizontal

# "NOTE: both array should be same and the number of rows"
# hori = np.hstack((arr1, arr2))
# print(hori)
hori = np.hstack((arr1, arr2, arr1, arr2))
# print(hori)

# "NOTE: both array should be same and the number of columns"
# ver = np.vstack((arr1, arr2))
# print(ver)
ver = np.vstack([arr1, arr2, arr1, arr2])
# print(ver)

# dstack: stacking along the height
# "NOTE: both array should be same and the number of elements in rows and columns should be same"
height = np.dstack((arr1, arr2))
# print(height)  # all the elements of arr1 will be in 1 column and arr2 in 2 column


# " S p l i t i n g " breaking array in multiple array
arr = np.array([1, 2, 3, 4, 5, 6])
# print(np.split(arr, 6))


# " S e a r c h i n g  and  s o r t i n g "
ar = np.array([1, 2, 3, 4, 5, 6, 4, 6, 6, 7, 9, 4])
# print(np.where(ar == 6))  # return the index value
# print(np.where(ar > 6))
# print(np.sort(ar))
# print(-np.sort(-ar))  # descending order

# " Any() and All() "
a = np.array([2, 5, 9, 6, 3, 7])
# print(np.any(a % 2 == 0))
# print(np.all(a % 2 == 0))


# " arange() " it will array of the given range
a1 = np.arange(10)
# print(a)
# print(np.reshape(a1, [2, 5]))  # you can create a matrix according to the number of elements
print(np.resize(a1, (3, 7)))  # free to create any dimension array
