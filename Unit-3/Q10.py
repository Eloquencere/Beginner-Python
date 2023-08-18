file = open("Shopper_list.txt", "r")
lines = file.readlines()
file.close()

file = open("revread.txt", "w+")
for i in lines[::-1]:
    file.write(i)
file.close()
