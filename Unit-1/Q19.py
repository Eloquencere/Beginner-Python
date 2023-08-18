dig=0
for i in range(3,-1,-1):
    if(i==0):
        dig+=(int(input("Enter leftmost digit: ")))*2**i
    else:
        dig+=(int(input("Enter next digit: ")))*2**i
print(dig)