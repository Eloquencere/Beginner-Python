lst=[1,2,3,3,3,3,4,5]
new=[]
for ele in lst:
    if ele not in new:
        new.append(ele)
print(new)
