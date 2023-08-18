file = open("words.txt", "r")
for i in file.readlines():
    if "msrit" in i:
        print(i)
file.close()
