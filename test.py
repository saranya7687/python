arn = "arn:aws:iam::123456789012:user/john"
print(arn.split("/") [1]) # Split and print the username

str1 = "jash"
str2 = "van"
result = str1 + "" + str2
print(result) # + sign for concatination of two strings

text = "jashvan"
length = len(text)
print(length) # Print no of characters in line

text = "ashvan"
case1 = text.upper()
case2 = text.lower()
print(case1)
print(case2) # upper and lower case in-built function

text = "Python is awesome"
newtext = text.replace("awesome" , "great")
print(newtext) #replace in-built function for string

text = "     some spaces around   "
newtext = text.strip() # strip removes empty spaces
print(newtext)
print(text)

text = "Python is good"
substring = text[2:5] # prints character between 2 and 5
print(substring)

num = 3.44444444
print(round(num, 2)) # in-built round off function for float data type

import re
text = "brown fox"
pattern = r"brown"
search = re.search(pattern , text)
if search:
    print("yes" , search.group())
else:
    print("not found")
       