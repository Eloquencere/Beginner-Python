def first2last2(string):
    if(len(string)<2):
        return ""
    else:
        return string[:2]+string[-2:]
