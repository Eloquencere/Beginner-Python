pwd=input("Enter password: ")
low=0
up=0
spechar=0
num=0
if(len(pwd)>=6 and len(pwd)<=16):
    for i in pwd:
        if(i.isupper()):
            up=1
        elif(i.islower()):
            low=1
        elif(i.isnumeric()):
            num=1
        elif(i in "@#$"):
            spechar=1
if(up and low and num and spechar):
    print("Valid")
else:
    print("Invalid")