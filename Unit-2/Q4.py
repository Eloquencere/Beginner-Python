def common(lst1,lst2):
    for i in lst1:
        if(i in lst2):
            return True
    return False
print(common([1,2,3],[4,5,6]))