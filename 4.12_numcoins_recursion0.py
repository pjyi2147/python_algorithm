def recMC(coinValueList, change, count):
    minCoins = change
    print('I am runnning! %d' % count)
    if change in coinValueList:     #change is in coinlist 
        return 1                    #only one coin needed!

    else: 
        count += 1
        for i in [c for c in coinValueList if c <= change]:   #coins smaller than change
            numCoins = 1 + recMC(coinValueList, change-i, count)     #subtract it and call fuction recursively
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

print(recMC([1,5,10,21,25], 22, 0))