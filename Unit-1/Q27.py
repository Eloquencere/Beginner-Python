deci=int(input("Enter a number: "))
bin=""
while(deci!=0):
    bin+= str(deci%2)
    deci//=2
print(bin[::-1])