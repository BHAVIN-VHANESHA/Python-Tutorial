tup = ()
# print(tup)  # empty tuple

tup1 = (1, 2, 3)
# print(tup1)
# print(tup1[0:2])  # last index is exclusive

x = ('a',)
# print(type(x))
y = ('a')
# print(type(y))

tup2 = tuple("bhavin")
# print(tup2)  # list of char
# print(tup2[1:4])
# tup2[0] = 'B'  # error
# print(tup2)
upd_tup2 = ('B',) + tup2[1:]
# print(upd_tup2)
# print(tup1+tup2)

var = (0, 1, 2) < (0, 3, 4)
# print(var)

m = ('have', 'fun')
a = m
b = m
# print(a, b)
# print(type(a))
# print(type(b))
a, b = m
# print(a, b)
# print(a)
# print(b)
# print(type(a))
# print(type(b))


# ''' tuple functions
tup3 = (1, 'b', 9.5, "ghanu", 3+2j, True, 0)
# print(tup3[5])
# print(tup3[6])
# print(len(tup3))
# print(tup3.count(1))
# chng = tup3[4] = False  # error bcoz tuples are immutable
# print(chng)
# '''
