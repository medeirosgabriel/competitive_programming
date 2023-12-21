class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        isPal = [[False for _ in range(n)] for _ in range(n)]
        cut = [0 for _ in range(n)]
        for i in range(n):
            min_ = i
            for j in range(i + 1):
                if (s[i] == s[j] and (i - j < 3 or isPal[j + 1][i - 1])):
                    isPal[j][i] = True
                    min_ = 0 if j == 0 else min(min_, cut[j - 1] + 1)
            cut[i] = min_
        return cut[n - 1]
