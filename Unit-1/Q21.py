low=int(input("Enter the lower limit"))
high=int(input("Enter the upper limit"))
for i in range(low,high+1):
    p=str(i)
    flag=1
    for j in range(len(p)):
        if(int(p[j])%2!=0):
            flag=0
            break
    if(flag):
        print(i,end=",")