def listsum(alist):
    if len(alist) == 1:
        return alist[0]

    else:
        return alist[0] + listsum(alist[1:])



print(listsum([1,4,3,4,234]))
