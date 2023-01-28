# opens the file for writing
f = open("myfile.txt", "w")
print("enter text (type # when done)")
s = ''
while s != '#':
    s = input()
    f.write(s + "\n")

f.close()
