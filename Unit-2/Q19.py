diction = {}

for i in range(3):
    a = input("Enter key: ")
    b = input("Enter value: ")

    diction[a] = b


val_list=[]
val_list=list(diction.values())

count=0
new_list=[]
for ele in val_list:
    if(ele not in new_list):
        count = count+1
        new_list.append(ele)
        
print(count)