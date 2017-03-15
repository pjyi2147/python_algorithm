#pascal's triangle 
import math as m

def combination(n,r):
    c = m.factorial(n) // m.factorial(r) // m.factorial(n-r) 
    return c

def pascaltri(k):
    for i in range(0, k+1):
        string = " "*(k-i) 
        if i == 0:
            string += '1'
        else:
            for j in range(i+1):
                string += str(combination(i,j))
                string += " "
        print(string)

pascaltri(5)