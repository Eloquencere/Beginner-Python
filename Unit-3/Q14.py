file = open("words.txt", "r")
for i in file.readlines():
    if "snake" in i:
        print(i)
file.close()
