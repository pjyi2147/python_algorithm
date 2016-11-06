import time
from random import randrange


def comparison1(lst):
    overallmin = lst[0]
    for i in lst:
        if i < overallmin:
            overallmin = i
    return overallmin

def comparison2(lst):
    overallmin = lst[0]
    for i in lst:
        issmallest = True
        for k in lst:
            if i > k:
                issmallest = False

        if issmallest:
            overallmin = i
    return overallmin

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(comparison1(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize, end-start))

    
