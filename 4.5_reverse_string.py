#4.5 reverse String
def revStr(string):
    if len(string) == 1:
        return string

    else:
        return revStr(string[1:]) + string[0]


print(revStr('I do not like'))
