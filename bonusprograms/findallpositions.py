s = input("enter a string")

sub = input("enter the substring to find")

found = False
pos = -1
length = len(s)
while True:
    pos = s.find(sub, pos+1, length)
    if pos == -1:
        break
    print("Found the substring at position ", pos)
    found = True

if found == False:
    print("Substring not found")
