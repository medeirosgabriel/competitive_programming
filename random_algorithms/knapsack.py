#Function to return max value that can be put in knapsack of capacity W.
def knapSack(W, wt, val, n):
	dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
	for i in range(n + 1):
		for cap in range(W + 1):
			if (i == 0 or cap == 0):
				dp[i][cap] = 0
			elif (wt[i - 1] < cap):
				dp[i][cap] = max(val[i - 1] + dp[i - 1][cap - wt[i - 1]], dp[i - 1][cap])
			else:
				dp[i][cap] = dp[i - 1][cap]
	return dp[n][W]

result = knapSack(4, [4,5,1], [1,2,3], 3)
print(result)
