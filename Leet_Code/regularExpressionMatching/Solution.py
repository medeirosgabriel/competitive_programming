class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]
        dp[0][0] = True
        for i in range(ls + 1):
            for j in range(1, lp + 1):
                if (p[j - 1] == "*"):
                    # a a  OR a a
                    # a *     . *
                    dp[i][j] = dp[i][j - 2] or (i > 0 and dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

        return dp[ls][lp]
