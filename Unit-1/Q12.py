x=input("Enter a word: ")
diction={}
for i in x:
    if(i in diction):
        diction[i]+=1
    else:
        diction[i]=1
print(diction)