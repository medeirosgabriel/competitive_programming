class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for l in range(n - 1, -1, -1): # Start of string
            dp[l][l] = 1
            for r in range(l + 1, n): # End of string
                if (s[l] == s[r]):
                    dp[l][r] = dp[l + 1][r - 1] + 2
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])

        return dp[0][n - 1]

