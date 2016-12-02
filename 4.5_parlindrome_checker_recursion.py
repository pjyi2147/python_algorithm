#4.5 palindrome checker
def removeWhite(s):
    s = s.split()
    s = "".join(s)
    return s

def revStr(string):
    if len(string) == 1:
        return string

    else:
        return revStr(string[1:]) + string[0]

def isPal(s):
    s = removeWhite(s).lower()
    if s == revStr(s):
        return True
    return False


print(isPal("Able was I ere I saw Elba"))
