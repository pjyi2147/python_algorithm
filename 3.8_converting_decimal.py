#3.8 converting Decimal to binary numbers
from pythonds.basic.stack import Stack

def divideBy2(num):
    remStack = Stack()

    while num > 0:
        remStack.push(num % 2)

        num = num // 2

    binstring = ""
    while not remStack.isEmpty():
        binstring = binstring + str(remStack.pop())

    return binstring

print(divideBy2(54))
print(divideBy2(233))
