x=input("Enter a string: ")
y=x[0]
for i in x[1:]:
    if(i==x[0]):
        y+="$"
    else:
        y+=i
print(y)