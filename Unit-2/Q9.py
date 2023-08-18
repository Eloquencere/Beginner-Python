def common(diction1,diction2):
    diction3={}
    for i in diction1.keys():
        if(i in diction2.keys()):
            for j in diction1.values():
                if j in diction2.values():
                    diction3[i]=j
    print(diction3)

common({"a":1,"b":3},{"b":2,"e":7})