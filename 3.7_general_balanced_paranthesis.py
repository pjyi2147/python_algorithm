#3.7 general balanced paranthesis
from pythonds.basic.stack import Stack

def parChecker(sampleString):
    s = Stack()
    index = 0
    Balance = True 
    while index < len(sampleString) and Balance:
        string = sampleString[index]
        if string in '([{':
            s.push(string)

        else:
            if s.isEmpty():
                Balance = False

            else:
                top = s.pop()
                if not matches(top, string):
                    Balance = False

        index = index + 1

    if Balance and s.isEmpty():
        return True

    else:
        return False


def matches(open, close):
    open_sets = '([{'
    close_sets = ')]}'
    return open_sets.index(open) == close_sets.index(close)

print(parChecker('[]()()()'))
print(parChecker('[][][[[[[]][}}}}[{}{}[}()(){}{}{}'))
