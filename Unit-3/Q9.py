def prime(lst):
    count=0
    for i in lst:
        flag=0
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break
        if((not flag and i!=1) or i==2):
            count+=1
    return count

lst=[1,2,3,4,5,6,7,8,9,11,13]
print(prime(lst))
