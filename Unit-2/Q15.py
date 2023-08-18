def gen():
    diction={}
    for i in range(1,20+1):
        diction[i]=i**2
    return diction
print(gen())