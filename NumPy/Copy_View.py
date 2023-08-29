import numpy as np

arr = np.array([1, 5, 7, 9, 8, 6, 4])
x = arr.copy()  # copy is the temporary change, it does not change original array
# print(x)
x[4] = 10
# print(x)
# print(arr)

y = arr.view()  # view make changes in original array
# print(y)
y[4] = 2
# print(y)
# print(arr)


# " I t e r a t i o n "
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# for i in arr1:  # this returns the array
    # print(i)
# for i in arr1:
    # for j in i:  # this returns the elements
        # print(j)  # if the dimension increases than complexity will increase so below given is the good way to print
                    # elements
# for i in np.nditer(arr1):
#     print(i)
for i in np.nditer(arr1[:1]):  # indexing
    print(i)
