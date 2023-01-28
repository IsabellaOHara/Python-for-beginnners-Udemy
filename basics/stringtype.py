s = "I am awesome"
print(s)

s1 = """I am 
the creator
of this script"""
print(s1)

# indexing to find characters
print(s[0])
print(s[6])


# displays the string twice - repetition
print(s*2)

# length of string
print(len(s1))
print(len(s))

# slicing [inclusive:exclusive
print(s[0:5])
# will start from beginning
print(s[:8])
# starts from the end - -1 is the last character
print(s[-3:-1])

# step value - here will do alternate characters - jumps 2 characters
print(s[0:9:2])
# to reverse a string
print(s[15::-1])
print(s[::-1])

# strip the spaces
# from end and beginning
t = "  you are awesome   "
print(t.strip())

# leading (left) white spaces gone
print(t.lstrip())

# right side spaces stripped
print(t.rstrip())

# find - locate substring in a string - start and end character - if cant find will be -1
print(s.find("awe", 0, len(15)))
print(s.count("a"))
# replace old with new
print(s.replace("awesome", "super"))

print(s.upper())
print(s.lower())
print(s.title())
