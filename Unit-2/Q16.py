def char_freq(string):
    diction={}
    for i in string:
        if(i in diction):
            diction[i]+=1
        else:
            diction[i]=1
    for key in diction:
        print(key+","+str(diction[key]),end=" ")
char_freq("Mississippi")