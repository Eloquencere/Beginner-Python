file = open("words.txt", "r")
longest = ""
for i in (file.read()).split():
    if len(longest) < len(i):
        longest = i
print(longest)
file.close()
