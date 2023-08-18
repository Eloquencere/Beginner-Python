def number(string):
    up=0
    low=0
    for i in string:
        for j in i:
            if j.isupper():
                up+=1
            elif j.islower():
                low+=1 
    print(up,low)
number('The quick Brown Fox')