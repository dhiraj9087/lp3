def kanpsack(w,a,b):
    n=len(a)
    dp=[[0]*(w+1) for _ in range(n)]
    for i in range(a[0],w+1):
        dp[0][i] = b[0]
    for i in range(1,n):
        for j in range(1,w+1):
            nottake = dp[i-1][j]
            take = float('-inf')
            if j>=a[i]:
                take = b[i]+dp[i-1][j-a[i]]
            dp[i][j] = max(take,nottake)
    print(dp[n-1][w])
b=[60,100,120]
a=[10,20,30]
w=50
print(kanpsack(w,a,b))