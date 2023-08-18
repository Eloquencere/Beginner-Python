file = open("Phone_Book.txt", "r")
x = file.readlines()
print(sorted(x))
file.close()
