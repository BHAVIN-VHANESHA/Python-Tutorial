# Lambda function ao anonymous function
# it is one line function

# minus = lambda x, y: x - y
# print(minus(5,7))

def firstindex(a):
    return a[1]


a = [[1, 14], [5, 6], [8, 23]]
# a.sort(key=firstindex) # it takes the keys length
a.sort(key=lambda x: x[1])
print(a)
