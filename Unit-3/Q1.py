# Create phonebook and input values
file = open("Phone_Book.txt", "a")
for i in range(5):
    name = input("Enter name: ")
    number = int(input("Enter phone number: "))
    file.write(f"{name}\t{number}\n")
file.close()

# Read contents, sort them and store in variable x
file = open("Phone_Book.txt", "r")
x = file.readlines()
x = sorted(x)
file.close()

# Rewrite sorted contents into the file
file = open("Phone_Book.txt", "w")
for i in range(len(x)):
    file.write(x[i])
file.close()
