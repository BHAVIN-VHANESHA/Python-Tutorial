#  " SYNTAX: pd.DataFrame(data, index, columns, dtype, copy) "

import pandas as pd
import numpy as np

#  CREATING DataFrame by different methods: list, dict, ndarrays, series, another dataframe
# empty dataframe
df = pd.DataFrame()
# print(df)

# NOTE: All arrays must be of the same length

# by list
data = [5, 96, 20, 55, 34, 81]
# df_list = pd.DataFrame(data)
df_list = pd.DataFrame(data, index=['a', 's', 'd', 'f', 'g', 'h'], columns=['A'])
# print(df_list)
data1 = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10],
        [11, 12]
    ]
]
# df_list1 = pd.DataFrame(data1)
df_list1 = pd.DataFrame(data1, columns=["c1", "c2", 'c3'], index=['a1', 'a2'])  # changes the column & index names
# print(df_list1)


# DICTIONARY  -  NOTE: # by changing the column name(keys) the result will be NaN for all values bcoz in dict keys
# are the column names
dict_data = {"name": ["bhavin", "kevin", "ram"], "age": ["23", "22", "21"]}
dict_df = pd.DataFrame(dict_data)
# dict_df = pd.DataFrame(dict_data, index=["a", "b", "c"])
# dict_df = pd.DataFrame(dict_data, columns=["a", "b", "c"])
# dict_df = pd.DataFrame(dict_data, index=["a", "b", "c"], columns=['first', 'second'])
# print(dict_df)


#     SERIES  -  NOTE: in series
s_data = {"marks1": pd.Series([63, 96, 45, 74], index=['test1', 'test2', 'test3', 'test4']),
          "marks2": pd.Series([50, 65, 90, 78], index=['ptest1', 'test2', 'ptest3', 'test4'])}
s_df = pd.DataFrame(s_data)
# s_df = pd.DataFrame(s_data, columns=['a', 'b', 'c', 'd'])
# s_df = pd.DataFrame(s_data, index=['a', 'b', 'c', 'd'])
# s_df = pd.Series(s_data, index=['a', 'b', 'c', 'd'])
# s_df = pd.DataFrame(s_data, columns=['a', 'b', 'c', 'd', 'e'], index=['A', 'B', 'C'])  # new df created
# print(s_df)
sd_data = ([
               {"A": 1, "B": 2, "C": 3},
               {'D': 4, 'E': 5, 'F': 6},
               {"G": 7, "H": 8, "I": 9}
           ],
           [
               {'a': 10},
               {'b': 20, 'c': 30}
           ])
# sd_df = pd.DataFrame(sd_data)
sd_df = pd.DataFrame(sd_data, index=['X', 'Y'], columns=["x", "x", "x"])  # in list of dict index and column name can
# be change
# print(sd_df)
# print(sd_df.size)
# print(sd_df.shape)
# print(sd_df.ndim)

# IMP
se_dfd = {'A': [
    [1, 2, 3],
    [4, 5, 6]
],
    'B': [
        [7, 8, 9],
        [4, 5, 6]
    ]
}
se_dfs = [
    {'A': [
        [1, 2, 3],
        [4, 5, 6]
    ],
        'B': [
            [7, 8, 9],
            [4, 5, 6]
        ]}
]
d = pd.DataFrame(se_dfd)
dfs = pd.DataFrame(se_dfs)
s = pd.Series(se_dfs)
# print(d)
# print(dfs)
# print(s)
