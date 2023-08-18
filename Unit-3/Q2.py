file = open("Shopper_list.txt", "w")
for i in range(3):
    file.write(input("Enter data: ") + "\n")
file.close()

file = open("Shopper_list.txt", "r")
lines = file.readlines()
big_list = []
for i in lines:
    p = i.split(",")
    big_list.append(p)
print(big_list)
file.close()
