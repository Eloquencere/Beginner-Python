row=int(input("Enter the number of rows: "))
column=int(input("Enter the number of columns: "))
lst=[[0 for y in range(column)] for x in range(row)] #list comprehension
for i in range(row):
    for j in range(column):
        lst[i][j]=i*j
print(lst)