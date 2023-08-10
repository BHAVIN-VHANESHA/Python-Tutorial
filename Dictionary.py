# search = input("enter the word: ")

# dict = {"bhavin": "hi ma name is bhavin i am a programmer", "beguiling": "charming and attractive"}

# print(dict[search])


word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
else:
    d[c] += 1
print(d)
