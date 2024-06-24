class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (word1[i - 1] == word2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1], # replace
                        dp[i][j - 1], # insert
                        dp[i - 1][j] # delete
                    ) + 1
        return dp[m][n]

'''
def minDistance(self, word1: str, word2: str) -> int:
        def helper(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if word1[i - 1] == word2[j - 1]:
                return helper(i - 1, j - 1)
            return 1 + min(helper(i - 1, j), min(helper(i, j - 1), helper(i - 1, j - 1)))

        return helper(len(word1), len(word2))
'''
