credit=int(input("Enter college credits: "))
if(credit>90):
    print("Senior Status")
elif(credit>60):
    print("Junior Status")
elif(credit>30):
    print("Sophomore Status")
else:
    print("Freshman Status")