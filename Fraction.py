def gcd(m,n): 
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

        
class Fraction:
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        return str(self.num)+"/"+str(self.den)
 
    #4 basic arithematic operations:

    def __radd__(self, other):
        newnum = self.num + other * self.den
        newden = self.den
        
        return Fraction(newnum, newden)       
    
    def __add__(self,otherfraction):
        
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum,newden)
    
    def __iadd__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den

        return Fraction(newnum,newden)
    
    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum,newden)
    
    def __mul__(self, otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den

        return Fraction(newnum,newden)

    def __truediv__(self, otherfraction):
        newnum = self.num*otherfraction.den
        newden = self.den*otherfraction.num

        return Fraction(newnum, newden)


    
    #comparisons 
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __lt__(self, otherfraction):                # x < y
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den
        if newnum * newden < 0:
            return True
        else:
            return False
    
    def __le__(self, otherfraction):                # x <=  y
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den
        if newnum * newden <= 0:
            return True
        else:
            return False
    
    def __ne__(self, other):                        # x != y
        if self.__eq__(other):
            return False
        else:
            return True

    def __gt__(self, otherfraction):                # x > y
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den
        if newnum * newden > 0:
            return True
        else:
            return False
    
    def __ge__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den
        if newnum * newden >= 0:
            return True
        else:
            return False
    
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

f1 = Fraction(3,6)
f2 = Fraction(25,16)
k = 13
print(f1)
print(f2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1.getNum())
print(f1.getDen())
print(f1)
print(f1 != f2)
print(f1 > f2)
print(f1 < f2)
print(f1 >= f2)
print(f1 <= f2)
print(f1 == f2)
print(repr(f1))
print(k + f1)
print(repr(Fraction(3,5)))
f1 += f2
print(f1)
