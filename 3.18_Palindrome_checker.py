#3.18 Palindrome-Checker
from pythonds.basic.deque import Deque

def checker(string):
    charqueue = Deque()

    for char in string:
        charqueue.addRear(char)

    
    stillEqual = True

    while charqueue.size() > 1 and stillEqual:
        if charqueue.removeFront() != charqueue.removeRear(): stillEqual = False

    return stillEqual


print(checker('asdfdsa'))
print(checker('Patrick'))


