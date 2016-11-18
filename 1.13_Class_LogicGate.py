class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()
        
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source

        elif self.pinB == None:
            self.pinB = source
            
        else:
             raise RuntimeError("Error: NO EMPTY PINS")
        
class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
    
        else:
             raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

class NorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 0
        else:
            return 1

class NandGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == b:
            return 0
        else:
            return 1

class PassGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPin()
        return a

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def main1():    
    g1 = AndGate('G1')
    g2 = AndGate('G2')
    # Not ((A and B) or (C and D))
    g3 = OrGate('G3')
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    g4 = NotGate('G4')
    c3 = Connector(g3,g4)
    print(g4.getOutput())

def main2():
    # NOT(A and B) and NOT (C and D)
    k1 = NandGate('K1')
    k2 = NandGate('K2')
    k3 = AndGate('K3')
    c1 = Connector(k1,k3)
    c2 = Connector(k2,k3)
    print(k3.getOutput())
    
def half_adder():
    A = PassGate('a')
    B = PassGate('b')
    x1 = XorGate('x1')
    a1 = AndGate('a1')
    c1 = Connector(A, x1)
    c3 = Connector(A, a1)
    c2 = Connector(B, x1)
    c4 = Connector(B, a1)
    Sum = x1.getOutput()
    Carry = a1.getOutput()
    print('Sum =', Sum, "Carry =", Carry)



#number inputs
half_adder()
"""
main1()
main2()
"""
