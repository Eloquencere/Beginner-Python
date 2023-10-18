from math import ceil

rows = int(input("Enter number of rows: "))
spaces = (ceil(rows / 2)) - 1


def AddSpaces(space):
    print(end=" " * (space + 1))


dots = 1
for x in range(ceil(rows / 2)):
    AddSpaces(spaces)
    for y in range(dots):
        print("*", end="")
    print("")
    spaces -= 1
    dots += 2  # one on either side

limit = rows - (ceil(rows / 2)) + 1 if (rows % 2 == 0) else rows - (ceil(rows / 2)) + 2
for x in range(limit):
    AddSpaces(spaces)
    for y in range(dots):
        print("*", end="")
    print("")
    spaces += 1
    dots -= 2  # one on either side
