#3.8 base_converter
from pythonds.basic.stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    
    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base

        remStack.push(digits[rem])
        decNumber = decNumber // base

    baseNum = ""
    while not remStack.isEmpty():
        baseNum = baseNum + remStack.pop()

    return baseNum

print(baseConverter(25,8))
print(baseConverter(256,16))
print(baseConverter(26,26))



