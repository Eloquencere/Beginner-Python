def sublist(lst1,lst2):
    if(str(lst2)[1:-1] in str(lst1)[1:-1]):
        return True
    else:
        return False
print(sublist([1,2,3,4,5,6],[4,5]))