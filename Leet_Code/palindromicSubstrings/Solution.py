class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        c = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for r in range(n):
            dp[r][r] = True
            c += 1
            for l in range(r):
                if (s[l] == s[r] and (r - l <= 2 or dp[r - 1][l + 1])):
                    dp[r][l] = True
                    c += 1
        return c
