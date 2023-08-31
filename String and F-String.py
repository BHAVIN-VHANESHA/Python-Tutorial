""" F String
firstname = "bhavin"
lastname = "vhanesha"
a = "my name is {0} {1}"
# a = "my name is {1} {0}"
result = a.format(firstname, lastname)
print(result)

a = f"my name is {firstname} {lastname}"
# print(a)
# """


''' update string char
greet = "hello"
print(greet[0])
greeting = 'j' + greet[1:]
print(greeting)
# '''


''' operations on string
n1 = '3'
n2 = '4'
print(n2+n1)
print(len(n1+n2))
print(n1*3)

st = "bhavin"
print(st[5])
last = st[len(st) - 1]
print(last)
print('a' in st)
print('e' in st)
c = 'c' in st
print(c)
# '''


''' string functions and parsing
str1 = "BhAvIn"
str2 = 'VhAnEsHa'
print(str1.upper())
print(str2.upper())
print(str1.lower())
print(str2.lower())
print(str1.join(str2))

str3 = "   BhAvIn VhAnEsHa   "
print(str3.split())  # create list of words
print(str3.split('delimiter'))  # split space using space

print(str3)
print(str3.strip())  # remove whitespace from left and right side
print(str3.rstrip())  # remove whitespace from right side
print(str3.lstrip())  # remove whitespace from left side

print(str1.isalpha())
print(str2.isdigit())

str4 = "   "
print(str4.isspace())
print(str3.isspace())

str5 = '20IT496'
print(str5.isalnum())
print(str2.isalnum())
print(str3.isalnum())

str6 = "Hi my name is bhavin vhanesha. I study in IT department at BVM in VVN"
print(str6.startswith('hi'))
print(str6.startswith('Hi'))
print(str6.startswith('H'))
print(str6.endswith("N"))
print(str6.endswith("VVN"))

print(str6.find('is'))  # returns the first matched index value
print(str6.find('I'))
print(str6.find('a', 6))  # start searching from 6th index value

print(str6)
print(str6.replace('Hi', "Hello"))

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
index = data.find('@')
print(index)
space = data.find(" ", index)
print(space)
host = data[index + 1:space]
print(host)
zero = data.find('0')
print(zero)
sec = data.find(' ', zero)
print(sec)
# time = data[zero + 1:sec]
time = data[zero:sec]
print(time)

str7 = 'bhavin vhanesha'
print(str7.capitalize())  # makes first char capital
# '''


'''  count occurrence of chars
def count_characters(string, char_count={}):
    if string == "":
        return char_count

    char = string[0]
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

    return count_characters(string[1:], char_count)


print(count_characters("bhavinvhanesha"))
# '''
