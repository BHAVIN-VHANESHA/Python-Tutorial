""" set methods and functions
a = set()
print(a)
a = {1, 2, 3}
print(a)
print(type(a))
a.add(4)
a.add(5)
print(a)

list1 = [60, 70, 80]
a.update(list1)
print(a)

print(len(a))
print(max(a))
print(min(a))
print(sorted(a))
print(sum(a))

a.discard(70)
print(a)

a.remove(80)
print(a)

a.pop()
print(a)
# """


''' set operations
A = {1, 2, 3, 4, 5}
B = {3, 5, 6, 8, 1}
print(A | B)
print(A.union(B))

print(A & B)
print(A.intersection(B))

print(A - B)
print(A.difference(B))

print(A ^ B)
print(A.symmetric_difference(B))

print(A.issubset(B))
print(B.issubset(A))

print(B.issubset(B))
print(A.issubset(A))

print(A.issuperset(B))
print(B.issuperset(A))

print(A.issuperset(A))
print(B.issuperset(B))
# '''


''' frozenset:- it is ordered set
A = {3, 5, 6, 8, 1}
B = frozenset(A)
print(B)
A.add(4)
print(A)
# B.add(2)  # we cannot update frozenset as the name itself suggest
# '''


# ''' Time of execution of data types
from timeit import timeit

print(f'tuple: {timeit("(1,2,3,4,5)")}')
print(f'list: {timeit("[1,2,3,4,5]")}')
print(f'set: {timeit("{1,2,3,4,5}")}')
print(f'dict:', timeit("{1:'o', 2:'p', 3:'a', 4:'q'}"))
# '''
