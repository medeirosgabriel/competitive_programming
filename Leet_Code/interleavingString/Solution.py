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

## BACKTRACKING

class Solution(object):
    def backTracking(self, s1, i, s2, j, s3, k):
        if (k == len(s3)):
            return True
        r1, r2 = False, False
        if (i < self.ls1 and s1[i] == s3[k]):
            r1 = self.backTracking(
                s1, i + 1, 
                s2, j, 
                s3, k + 1
            )
        if (j < self.ls2 and s2[j] == s3[k]):
            r2 = self.backTracking(
                s1, i, 
                s2, j + 1, 
                s3, k + 1
            )
        return r1 or r2

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.ls1, self.ls2, self.ls3 = len(s1), len(s2), len(s3)
        if (self.ls1 + self.ls2 != self.ls3): return False
        return self.backTracking(s1, 0, s2, 0, s3, 0)
