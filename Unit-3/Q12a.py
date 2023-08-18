file = open("Shopper_list.txt", "r")
flag = 1
lines = []
while flag:
    line = file.readline()
    if line != "":
        lines.append(line)
    else:
        flag = 0
print(lines)
file.close()
