def char_freq(string):
    diction={}
    for i in string:
        if(i in diction):
            diction[i]+=1
        else:
            diction[i]=1
    print(diction)

char_freq("Mississippi")