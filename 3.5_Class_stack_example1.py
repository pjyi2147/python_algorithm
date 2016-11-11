from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystr):
    s= Stack()
    string = ""
    for i in mystr:
        s.push(i)

    for i in range(len(mystr)):
        string = string + s.pop()

    return string

        
testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
