def getways(n,c):
    dp=[0]*(n+1)
    dp[0]=1
    for coin in c:
        for x in range(coin,n+1):
            dp[x]+=dp[x-coin]
    return dp[n]
print(getways(3,[6,1,2,3]))