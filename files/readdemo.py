f = open("sample.txt", "r")
print(f.read()) # can pass in the number of characters you want to read
f.seek(0) # moves the file cursor back to the start
print(f.readline())
f.seek(0)
print(f.readlines()) # return list of all characters in file
f.close()
