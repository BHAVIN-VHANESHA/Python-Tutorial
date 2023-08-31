""" changing assigned values
A = 5
B = A
C = A + B
F = A+1 + B
D, E = 3, 5
print('value of a', A)
print('value of b', B)
print('value of c', C)
print('value of d', D)
print('value of e', E)
print('value of f', F)
# """


''' type conversion
in python every input is taken as string but eval convert the datatype of the input data

y = input()
print(y)
print(type(y))

x = eval(input())  
print(x)
print(type(x))
# '''


''' Use of end and sep
a = 'bhavin'
b = "vhanesha"
print(a, b, sep="_")
print(a, b, end='!')
# '''


''' Use of Operators
i = 10
j = 2
print(i + j)
print(i - j)
print(i * j)
print(i ** j)  # power
print(i / j)
print(i // j)  # floor division values
print(i % j)  # remainder
print(i & j)  # bitwise AND
print(i ^ j)  # bitwise XOR
print(i | j)  # bitwise OR
print(~i)  # bitwise NOT
print(~j)  # bitwise NOT
print(i >> j)  # right shift
print(i << j)  # left shift
# '''


'''
def add(a, b):
    return a + b


# assigning valur of add function to c
c = add(9, 6)


# passing function as parameter
def mul(c, d):
    return c * d


print(mul(c, 6))
# '''


''' function inside function
def Add(x, y):
    def ad(z):
        return z * 2

    return ad(x) + y


print(Add(2, 3))
# '''


'''
d = dict()

def word():
    stri = "bhavin"
    for i in stri:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)


word()
# '''


''' infinite loop
i = 0
sum = 0
while i < 9:
    if i % 4 == 0:
        sum += i
        i = i + 2
print(sum)
# '''


''' thinkable
for i in range(10):
    for j in range(i):
        print(i * j)
        print(i)
        print(j)
    print("\n")
# '''
