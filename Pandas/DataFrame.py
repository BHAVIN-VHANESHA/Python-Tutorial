#  " SYNTAX: pd.DataFrame(data, index, columns, dtype, copy) "

import pandas as pd
import numpy as np

#  CREATING DataFrame by different methods: list, dict, ndarrays, series, another dataframe
# empty dataframe
df = pd.DataFrame()
# print(df)

# by list
data = [5, 96, 20, 55, 34, 81]
df_list = pd.DataFrame(data)
# print(df_list)
data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df_list1 = pd.DataFrame(data1, columns=["c1", "c2", 'c3'])  # changes the columns names
# print(df_list1)

#    DICTIONARY
dict_data = {"name": ["bhavin", "kevin", "ram"], "age": ["23", "22", "21"]}
# dict_df = pd.DataFrame(dict_data)
dict_df = pd.DataFrame(dict_data, index=["a", "b", "c"])
# dict_df = pd.DataFrame(dict_data, index=["a", "b", "c"], columns=['first', 'second'])
# print(dict_df)


#     SERIES
s_data = {"marks1": pd.Series([63, 96, 45, 74], index=['test1', 'test2', 'test3', 'test4']),
          "marks2": pd.Series([50, 65, 90, 78], index=['ptest1', 'test2', 'ptest3', 'test4'])}
# s_df = pd.DataFrame(s_data)
# s_df = pd.DataFrame(s_data, columns=['a', 'b', 'c', 'd'])
s_df = pd.DataFrame(s_data, columns=['a', 'b', 'c', 'd'], index=['A', 'B'])
print(s_df)
# in dict series we cannot change the in the column name and index name we, so create series of dict
sd_data = [{"A": 1, "B": 2, "C": 3}, {'D': 4, 'E': 5, 'F': 6}, {"G": 7, "H": 8, "I": 9}]
sd_df = pd.DataFrame(sd_data)
# sd_df = pd.DataFrame(sd_data, index=['A', 'B', 'C'], columns=["1", "2", "3"])
print(sd_df)

