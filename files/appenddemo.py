f = open("sample.txt", "a+")
print("cursor is at", f.tell())
f.write("i am learning python for data engineering")
f.seek(0)
a = []
for line in f:
    a.append(line)
print(a)
f.close()
