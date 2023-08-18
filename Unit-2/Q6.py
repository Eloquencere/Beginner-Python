lst = ["Fire", "Speed", "Apple"]
vow = 0
for i in lst:
    for j in i:
        if j in "aeiou":
            vow += 1
print(vow)
