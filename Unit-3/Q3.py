file = open("Phone_Book.txt", "r")
diction = {}
letters = "abcdefghijklmnopqrstuvwxyz"

for i in letters:
    diction[i] = 0

for i in file.read():
    if i.lower() in letters:
        diction[i.lower()] += 1

print(diction)
file.close()
