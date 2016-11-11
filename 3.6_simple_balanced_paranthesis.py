#3.6 simple balanced paranthesis
from pythonds.basic.stack import Stack
def parChecker(sampleString):
    s = Stack()
    index = 0
    Balance = True 
    while index < len(sampleString) and Balance:
        string = sampleString[index]
        if string == '(':
            s.push(string)

        else:
            if s.isEmpty(): Balance = False

            else: s.pop()

        index = index + 1

    if Balance and s.isEmpty():
        return True

    else:
        return False


print(parChecker('((()()()())()()()))'))
print(parChecker('(()()()())'))
print(parChecker('()()()()'))
