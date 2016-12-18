#4.12 recursion method to make a minimum change maker
def recMC(coinValueList, change, knownResults):             #recursion minimun coins
    minCoins = change
    if change in coinValueList:                             #change is same with one of the coins!
        knownResults[change] = 1                            #there is only one way to solve this! 
        return 1                                            #only one coin then 
    elif knownResults[change] > 0:                          #if we know the minimum coins to make change
        return knownResults [change]                        #return it!
    else:                                                   #we need 2 coins at least!
        for i in [c for c in coinValueList if c <= change]:                 #for each coin
            numCoins = 1 + recMC(coinValueList, change-i, knownResults)     #we subtract them and recursion it again 
            if numCoins < minCoins:                         #new minimum way!
                minCoins = numCoins         
                knownResults[change] = minCoins             #we have to store this!               
    return minCoins


print(recMC([1,5,10,25], 63, [0]* 64))