n=int(input("Enter an upper limit: "))
susq=0
sqsu=0
for i in range(1,n+1):
    susq+=i
    sqsu+=i**2
susq**=2
print("Difference is", susq-sqsu)