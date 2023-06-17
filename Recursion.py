# recursion in python

# this is the iterative method
'''

def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


number = int(input("enter the nuber: "))

print(factorial(number))

'''


# recursion method
def factrecur(n):
    if n == 1:
        return 1
    else:
        return n * factrecur(n - 1)


number = int(input("enter the nuber: "))

print(factrecur(number))
