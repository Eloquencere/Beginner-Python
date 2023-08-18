a=int(input("Enter side 1: "))
b=int(input("Enter side 2: "))
c=int(input("Enter side 3: "))
if(a==b==c):
    print("Equilateral")
elif(a==b or a==c or b==c):
    print("Isoceles")
else:
    print("Scalene")