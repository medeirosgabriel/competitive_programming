class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        ls1, ls2, ls3 = len(s1), len(s2), len(s3)
        if (ls1 == 0): return s2 == s3
        if (ls2 == 0): return s1 == s3
        if (ls3 != ls1 + ls2): return False

        dp = [[False for _ in range(ls2 + 1)] for _ in range(ls1 + 1)]
        dp[0][0] = True

        for i in range(1, ls1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, ls2 + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]
        
        for i in range(1, ls1 + 1):
            for j in range(1, ls2 + 1):
                if (s1[i - 1] == s3[i + j - 1]):
                    dp[i][j] = dp[i - 1][j]
                if (s2[j - 1] == s3[i + j - 1]):
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        return dp[-1][-1]
        
