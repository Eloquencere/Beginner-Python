size=int(input("Enter number of numbers: "))
even=0
odd=0
for i in range(size):
    x=int(input("Enter a number: "))
    if(x%2==0):
        even+=1
    else:
        odd+=1
print("Even", even,"Odd", odd)