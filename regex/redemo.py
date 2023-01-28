import re

str = "Take 1 up One 23 idea. One idea 45 at a time"
str2 = "1-3-2019 hello my name is bella 12-11-2020"
result = re.search(r'O\w\w', str)
print(result.group())

result = re.findall(r'o\w\w', str)
print(result)

# only searches at the beginning of the string
result = re.match(r'T\w\w', str)
print(result.group())

# splitting the string wherever there are numbers
result = re.split(r'\d+', str)
print(result)

# sub method does a replace all
result = re.sub(r'one', 'two', str)
print(result)

result = re.findall(r'O\w{1,2}', str)
print(result)

# finding date
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str2)
print(result)

# special characters
result = re.search(r'^T\w*', str)
print(result.group())
