""" dictionary (key-value pair)
fruits = dict()  # empty dict
# print(fruits)

fruits['apple'] = 2
fruits['kiwi'] = 5
fruits['pineapple'] = 3
fruits['orange'] = 4
fruits['mango'] = 7
print(fruits)

fruits['apple'] = 6
print(fruits)

del fruits['orange']
print(fruits)

print(fruits.items())
fruits.clear()
print(fruits)
# """


''' tuple as key
number = {}
number['bhavin vhanesha'] = 7600270056
number['bhavin patel'] = 7600270096
print(number)
print(number['bhavin patel'])
# '''


''' how to copy list and dictionary
l1 = [1]
l2 = list(l1)
l1[0] = 10
print(l1)
print(l2)

d1 = {1: 10}
d2 = d1.copy()
d1[1] = 1
print(d1)
print(d2)
# '''


''' dict functions
dictionary = {0: 'zero', "a": 97, '20IT496': "bhavin", 6: 9, True: 'boolean value', "float": 10.0, -1: '-ve'}
print(dictionary)
print(len(dictionary))
print(dictionary.keys())
print(dictionary.values())

# chk = 0 in dictionary
# chk = -1 in dictionary
chk = 'hi' in dictionary
print(chk)

print(dictionary[6])
print(dictionary['20IT496'])

print(dictionary.get(True, 'sorry no match found'))
print(dictionary.get(int, 'sorry no match found'))

dictionary[0] = "False"
print(dictionary)

del dictionary[-1]
print(dictionary)

for keys in dictionary:
    print(keys)
# '''


''' convert dictionary into list
dictionary = {0: 'zero', "a": 97, '20IT496': "bhavin", 6: 9, True: 'boolean value', "float": 10.0, -1: '-ve'}
print(dictionary.items())
lis = list()
for keys, values in dictionary.items():
    lis.append((keys, values))
    # print(lis)
print(lis)
# '''


""" basic dictionary
search = input("enter the word: ")

dicts = {"bhavin": "hi my name is bhavin i am a programmer", "beguiling": "charming and attractive"}

print(dicts[search])
# """


''' count chars
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
else:
    d[c] += 1
print(d)
# '''


# ''' count words in file
file_name = input("enter the file name: ")
try:
    file = open(file_name)
except:
    print(f'{file_name} cannot be opened')
    exit()
counts = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
# '''
