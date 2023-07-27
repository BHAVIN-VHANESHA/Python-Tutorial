import re

# " Data Cleaning "
stri = ''' hi my name is bhavin, my contact number is +91-8780392112, you can call me anytime and in emergency you can
 contact me on number +91-7600270056'''
# number = re.findall('918780392112', stri)
# print(number)
# number = re.findall('\d', stri)
# print(number)  # prints the all single digit
# number = re.findall('\d+', stri)
# print(number)  # prints all the digits

# so the pattern we can find is first two digit country code and rest the number
number = re.findall('\d{2}-\d{10}', stri)  # ' \d+ ' : is used in authentication
print(number)
