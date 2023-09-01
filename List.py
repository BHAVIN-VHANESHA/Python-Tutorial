"""
list1 = []  # empty list
print(list1)

list1.insert(0, 10)
list1.insert(1, 20)
list1.insert(2, 30)
list1.insert(3, 40)
list1.insert(4, 50)
print(list1)

list2 = [1, 2.5, True, 'a', "bhavin", 3+2j]
print(list2)
list2.insert(0, '''multi-line string''')
print(list2)
# """


''' list operators
list3 = [1, 2, 3, 4]
list4 = [6, 7, 8, 9]

# new_list = list3 + list4

# new_list = list3 - list4   we cannot subtract one list from another
# new_list = list3[0] - 1

# new_list = list3 * list4   we cannot multiply one list with another
# new_list = list3 * 3  # here elements will not be multiply by 3 but the occurrence of list will be 3 times
# new_list = list3[0] ** 2  # power

# new_list = list3 / list4  we cannot divide one list with another
# new_list = list3[0] / 2
# new_list = list3[0] // 2  # floor division value

# new_list = list4[0] | 1
# new_list = list4[0] & 1
# new_list = list4[0] ^ 1
# new_list = list4[0] << 2
# new_list = list4[1] >> 2

new_list = list4[3] % 2

print(new_list)

check1 = 3 in list4
print(check1)
check2 = 3 in list3
print(check2)
# '''


''' string into list
str1 = "bhavin vhanesha"
str_list = list(str1)
print(str_list)
spl = str1.split()
print(spl)
# '''


''' traversing
list2 = [1, 2.5, True, 'a', "bhavin", 3+2j]
for i in list2:
    print(i)
# '''


''' identical and equality
"""
If two objects are identical, they are also equivalent,
but if they are equivalent, they are not necessarily identical.

Two lists are equivalent because they have the same elements 
but not identical because they are not same objects.
"""

x = [1, 2, 3]
y = x
print(f'y: {y}')
print(f'x: {id(x)}')
print(f'y: {id(y)}')

y[0] = 6  # here the element in list x will also be changed as the object is same
print(f'y: {y}')
print(f'y: {id(y)}')
print(f'x: {x}')
print(f'x: {id(x)}')

a = [96, "bhavin", 10.0]
b = [20, 'IT', 10.0]
c = [20, 'IT', 10.0]  # here the elements are same but object are different
print(f'a: {id(a)}')
print(f'b: {id(b)}')
print(f'c: {id(c)}')
# '''


''' list methods
list2 = [1, 2.5, True, 'a', "bhavin", 3+2j]

# list2.insert(2, False)
# print(list2)

# list2.append(list2[1])
# list2.append(list2)
# list2.append(96)
# print(list2)
# print(list2[8])
# list2[8] = -1
# print(list2)
# list2.append([96, 'IT'])
# print(list2)
# list2.append(["vhanesha"])
# list2.append("vhanesha")
# print(list2)


# list2.extend(list2)
# print(list2)
# list2.extend(["vhanesha"])
# list2.extend("vhanesha")
# print(list2)

list6 = [1, 1, 2.5, 0, True, True, False]

# print(list6.index(2.5))
# print(list6.index(True))  # value of true is 1
# print(list6.index(False))  # value of false is 0

# list6.remove(False)
# print(list6)
# list6.remove(1)  # Deletes the first occurrence
# print(list6)
# list6.remove(2.5)  # Deletes the first occurrence
# print(list6)
# list6.remove(True)  # value of true is 1, so it will remove 1 first
# list6.remove(list6[4])
# list6.remove(True)  # same as above onr
# print(list6)
# del list6[4]  # 'del' keyword can delete any element unlike 'remove' keyword
# print(list6)

# list6.pop(3)
# print(list6)

# list6.sort()
# print(list6)
# print(sorted(list6))
# print(sorted(list6, reverse=True))

# list6.reverse()
# print(list6)
# list2.reverse()
# print(list2)

# print(list6.count(1))
# print(list6.count(True))
# print(list6.count(False))
# print(list6.count(2.5))
# print(list2.count('a'))
# '''


''' list to string
li = ['hi', 'bro', 'here']
print(type(li))
stri = " ".join(li)
print(stri)
print(type(stri))
st = " lelo ".join(li)
print(st)
st = "_".join(stri)  # 🤯
print(st)
# '''


''' 2D list
list_2D = [[1, 2, 3], [4, 5, 6], [7, 8.9]]
print(list_2D[0])
print(list_2D[1])
print(list_2D[2])

print(list_2D[0][0])
print(list_2D[1][0])
print(list_2D[2][0])

x, y, z = list_2D
print(x, y, z)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
# '''


''' list comprehension
i = [1, 2, 3]
result = [x ** 2 for x in i]
print(result)
min_ = [n for n in i if n <= 2]
print(min_)
fruits = ['mango', 'dates', 'orange']
fruitss = [s.upper() for s in fruits if 'a' in s]
print(fruitss)
# '''


''' parsing lines using list
fhand = open('list.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[1])
# '''
