n=int(input("Enter limit: "))
lst=["Fire","Speed","Apple"]
new=[]
for i in range(len(lst)):
    if len(lst[i])<=n:
        new.append(lst[i])
print(new)