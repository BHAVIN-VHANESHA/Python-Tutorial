f = open("bhavin.txt", "r")
# print(f.read())

'''
content = f.read(6)
print(content)

content = f.read(6)
print(content)
'''

'''
so above if u call f.read() different times passing the same parameter the output will be different
'''

# for loop
# for line in f:
#     print(line, end="")  # here end is used to remove default line break

# read line by line
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline())
# print(f.readline())
# print(f.readline())

# to store lines in list
# print(f.readlines())


# writing in file
file = open("demo.txt", "w")
# file.write("hi i am piro programmer")
# print(file)

# adding content in file
# appendfile = open("demo.txt", "a")
# appendfile.write("my name is bhavin\n")

# reading and writing
rwfile = open("bhavin.txt", "r+")
print(rwfile.read())
rwfile.write("thank u")

f.close()
