#4.5 converting an integer to any base
def toStr(n, base):
    convertstring = '0123456789ABCEDF'
    if n < base:
        return convertstring[n]

    else:
        return toStr(n//base, base) + convertstring[n%base]


print(toStr(128,2))
