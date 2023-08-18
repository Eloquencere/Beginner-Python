x= list(input("Enter: "))
Digit=0
Letter=0
for i in range(len(x)):
    if(x[i].isalpha()):
        Letter+=1
    elif(x[i].isnumeric()):
        Digit+=1
print("Letters: ",Letter, "\nDigits: ", Digit)