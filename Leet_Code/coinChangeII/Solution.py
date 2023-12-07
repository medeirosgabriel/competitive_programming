class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1 # For amount 0, there is 1 way to solve the problem.. 0 coins
        for i in range(1, n + 1):
          for s in range(amount + 1):
              dp[i][s] += dp[i - 1][s]
              if (s - coins[i - 1] >= 0):
                dp[i][s] += dp[i][s - coins[i - 1]]

        return dp[n][amount]
