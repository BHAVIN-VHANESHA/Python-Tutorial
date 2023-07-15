f = open("bhavin.txt", "r")
# print(f.read())
# print(f.read(10))  # reads the 10 character
# print(f.tell())  # current position of the
# print(f.seek(20))  # change the current value of curser
# content = f.read()  # in order to print all the characters
# for i in content:
#     print(i)
# print(f.readline())  # first line will be read
# print(f.readlines())  # return a list of lines from the current position of curser


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
# file = open("demo.txt", "w")
# file.write("hi i am piro programmer")
# print(file)

# adding content in file
# appendfile = open("demo.txt", "a")
# appendfile.write("my name is bhavin\n")

# reading and writing
rwfile = open("bhavin.txt", "r+")  # r+ mode writes and appends it
print(rwfile.read())
rwfile.write("thank u\n")
print(rwfile.read())

f.close()
