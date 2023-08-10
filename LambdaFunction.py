# Lambda function an anonymous function
# it is one line function

minus = lambda x, y: x - y


# print(minus(5, 7))


def firstindex(a):
    return a[1]


a = (1, 0)
# print(firstindex(a))

a = [[14, 1], [5, 6], [4, 23]]
a.sort(key=firstindex)  # it takes the keys length
a.sort(key=lambda x: x[1])
# print(a)

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10]
print(list(filter(lambda x: x % 2 == 0, List)))
print(set(filter(lambda x: x % 2 == 0, List)))
print(list(map(lambda x: x + 2, List)))
print(set(map(lambda x: x + 2, List)))
print(list(map(lambda x: x % 2 == 0, List)))
print(tuple(map(lambda x: x % 2 == 0, List)))
