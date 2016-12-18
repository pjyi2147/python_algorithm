def dpMakeChange(coinList, change, coinUsed, minCoins):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change]

def printCoinUsed(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]                   #track what coin was used to make this value minimally
        print(thisCoin)                             #print it!
        coin = coin - thisCoin                      #redefine coin

def main():
    change = 64
    coinList = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (change + 1)
    minCoins = [0] * (change + 1)
    print("The lowest number of coins needed to make %d cents:" % change)
    print(dpMakeChange(coinList, change, coinsUsed, minCoins), "coins")
    print('These coins were used:')
    printCoinUsed(coinsUsed, change)
    print("the used list:")
    print(coinsUsed)

main()
