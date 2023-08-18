file = open("original_text", "r+")
diction = {"c": 0}
for i in file.read():
    if i == "c":
        diction[i] += 1
print(diction)
file.close()
