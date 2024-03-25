import re

# " Data Cleaning "
stri = ''' hi my name is bhavin, my contact number is +91-8789378520, you can call me anytime and in emergency you can
 contact me on number +91-7600270056. I am doing data structures course the language used is JAVA'''
# number = re.findall('91-8780392112', stri)
# print(number)
# number = re.findall('\d', stri)
# print(number)  # prints the all single digit
# number = re.findall('\d+', stri)
# print(number)  # prints all the digits
# all = re.findall("\??i", stri)
# print(all)

# so the pattern we can find is first two digit country code and rest the number
# number = re.findall('\d{2}-\d{10}', stri)  # ' \d+ ' : can be used in authentication
# print(number)

# for string
strii = "hi my name is bhavin, i am a programmer, contact me on number +91-7600270056"
serstr = re.search('^is', strii)  # we can confirm the string starting with
# print(serstr)
# serstr = re.search('is', strii)
# if serstr:  # if string with space then space is also going to be counted
#     print("matched")
# else:
#     print("not found")

# " Match " : it stores and return the first match value
str1 = "lion is the king of jungle, lion is not pet animal, lizard can be of many types"
# strm = re.match("l\w\w", str1)  # '\w':means the single character
strm = re.match("l\w+", str1)  # '\w':means the single character
# print(strm)                           # '\w+':means the word

# to match all the words starting with same character
# print(strm.group())


# " Split "
spli = re.split('\s', str1)
# spli = re.split('\s', str1, 5)
# print(spli)


# " Replace - (sub) " : re.sub(pattern, replaced pattern, string)
str2 = "cricket is my favourite game"
chan = re.sub("i", "f", str2, 1)  # here count means the number of occurrence of pattern you want to change
# print(chan)


# " Metacharacters "
str3 = "mumbai is the financial capital of india"
meta = re.findall("[a-g]", str3)  # finding in the range
# print(meta)
end = re.findall("india$", str3)
end1 = re.findall("\Ais", str3)
# print(end)
# print(end1)


# " Dot " it is used to join the search
st = "today is 31st july, today is monday"
dot = re.search("^today.+monday$", st)  # '*' is used to match single or whole word occurrence and also prints
# print(dot)                                      #  the stuff that does not match
# find = re.findall("t*", st)
find = re.findall("t+", st)
# find = re.search("t", st)
# print(find)
