x=0
sum=0
while True:
    x=input("Enter a number (<=100) or enter P to exit: ")
    if(int(x)<=100 and int(x)>=0):
        sum+=int(x);
    if(x=="P"):
        break
    
print ("sum is",sum)