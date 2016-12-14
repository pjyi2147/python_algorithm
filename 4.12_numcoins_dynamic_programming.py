# 4.12 dynamic programming way to create minimun coin changer
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):                               #starting from 1 cent
        coinCounts = cents                                      #giving change with pennies
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:      #if there is a smaller coin value than change
            if minCoins[cents-j] + 1 < coinCounts:              #if there is a smaller value of coins
                coinCounts = minCoins[cents-j] + 1              #change it!
                newCoin = j                                     #what coin was used
        minCoins[cents] = coinCounts                            #store the minimum value of coins
        coinsUsed[cents] = newCoin                              #store what was used
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print('They are:')
    printCoins(coinsUsed, amnt)
    print('The used list is as follows:')
    print(coinsUsed)

main() 