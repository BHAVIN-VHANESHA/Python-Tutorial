# it is a python library used while working with datasets
# some major functions are: analyze, cleaning, exploring the data, manipulation
import pandas as pd  # full-form of pandas is panel-datas
import numpy as np


# to check the version of the pandas
# print(pd.__version__)


# pandas has three data structures: series(1D), dataframe(2D and industries use these) and panel(3D)
# these pandas datastructures are built on numpy arrays so these are very fast

# NOTE: in pandas the row values can access by index values and column values can be access by column values

# " S E R I E S " : SYNTAX:- ps.series(data(arrays, dict, scalar), index, dtype)

#   CREATING
s = pd.Series()
# print(s)

# creating data using np array
arr_data = np.array([96, 63, 20, 50, 100, 74])
arr_s = pd.Series(arr_data)
# print(arr_s)  # prints default indexes count with values

# but index values can be changed
arr_sc = pd.Series(arr_data, index=[1, 2, 3, 4, 5, 6])
# print(arr_sc)

# creating data using dict
dict_data = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
dict_s = pd.Series(dict_data)
# print(dict_s)
dict_sc = pd.Series(dict_data, index=["f", "g", "h", "i", "j"])  # if we change the index values in dict then we get
# NaN values
# print(dict_sc)
dict_sc1 = pd.Series(dict_data, index=["d", "a", "f", "e", "c", "b"])  # if we rearrange the index values in dict
# then we get values assigned to it in the rearranged format
# print(dict_sc1)

# creating data using scalar
scalar_data = 96
scalar_s = pd.Series(scalar_data, index=[6, 7, 8, 9, 10])
# print(scalar_s)


#   UPDATING
upd_data = np.array([12, 45, -6, 0.9, 30, -0.5])
upd_s = pd.Series(upd_data)
# print(upd_s)
# print(upd_s[2])
# print(upd_s[-3:-1])  # -ve indexing starts with 1
# print(upd_s[-3:])  # -ve indexing starts with 1
# print(upd_s[:3])  # +ve indexing starts with 0

upd_dict_data = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
upd_dict_s = pd.Series(upd_dict_data, index=["d", "a", "f", "e", "c", "b"])
# while slicing in dict both the points are inclusive but in list the end point is exclusive
# print(upd_dict_s['a':'c'])  # prints data between two points
# print(upd_dict_s[["e", "f", 'b']])
upd_dict_s['f'] = 96
# print(upd_dict_s["f"])
# print(upd_dict_s, ["d", "a", "f", "e", "c", "b"])


#    BOOLEAN MASKING
boolmask = upd_dict_s > 20
# print(boolmask)  # returns boolean value
# print(upd_dict_s[upd_dict_s > 30])  # to return the values
# print(upd_dict_s[upd_dict_s > 30 or upd_dict_s == 10])
print(upd_dict_s.all(upd_dict_s>30) or upd_dict_s.all(upd_dict_s == 10))
# print(upd_dict_s.values)
# print(upd_dict_s.index)
# print(upd_dict_s['b'])
# print(upd_dict_s['b'] in upd_dict_s)  # bcoz in pandas row operation is done by index
# print('b' in upd_dict_s)


#     DELETE
delete = upd_dict_s.drop('c')
# print(delete)  # it does not delete element permanently
# print(upd_dict_s)
# to delete the element permanent
dele = upd_dict_s.drop(['c', "d"], inplace=True)
# print(dele)
# print(upd_dict_s)
# print(upd_dict_s * 2)  # temporary change
# print(np.power(upd_dict_s, 2))
# print(upd_dict_s ** 2)
# print(np.exp(upd_dict_s))
# print(upd_dict_s['a'] - 5)

