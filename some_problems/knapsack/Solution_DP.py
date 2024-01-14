def knapSack(cap, wt, val, n): 
    dp = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(cap + 1):
            if (i == 0 or w == 0):
                continue
            elif (wt[i - 1] <= w):
                dp[i][w] = max(
                        val[i - 1] + dp[i - 1][w - wt[i - 1]],
                        dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[i][w]
            

profit = [60, 100, 120]
weight = [10, 20, 30]
cap = 50
n = len(profit)
print(knapSack(cap, weight, profit, n))