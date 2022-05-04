N, W = map(int, input().split())

def knapsack(n, w)-> int:
    dp = [[0]*(w+1) for i in range(n+1)]
    for i in range(1, n+1):
        wi, vi = map(int, input().split())
        # j=0~w
        for j in range(w+1):
            if j - wi < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-wi]+vi)
            print(dp[i][j])
    return dp[n][w]

print(knapsack(N, W))


