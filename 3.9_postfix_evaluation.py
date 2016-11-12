#3.9 postfix_evaluation
from pythonds.basic.stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(token)

        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(op, operand1, operand2):
    if op == "*":
        return int(operand1) * int(operand2)
    elif op == "/":
        return int(operand1) / int(operand2)
    elif op == "+":
        return int(operand1) + int(operand2)
    elif op == "-":
        return int(operand1) - int(operand2)

print(postfixEval('7 8 + 3 2 + /'))
