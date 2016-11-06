import random

def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randint(0,len(alphabet) - 1)]

    return res

def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame += 1

    return numSame / len(goal)

def main():

    goalstring = "methinks it is like a weasel"
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring, newstring)
    times = 0
    while newscore < 1 and times < 1000000:
        if newscore >= best:
            print(newstring, newscore, times)
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring,newstring)
        times += 1


main()

                
            
    
