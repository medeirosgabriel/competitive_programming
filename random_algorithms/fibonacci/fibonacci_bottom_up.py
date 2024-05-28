'''
Bottom-up (tabulation): starts with the trivial solution and calculations 
are carried out until the optimal solution of the problem.
'''

def fibonacci_bottom_up(n):
  dp = [0] * (n + 1)
  dp[0] = 0
  dp[1] = 1

  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

  return dp[n]

n = 11
print(fibonacci_bottom_up(n))