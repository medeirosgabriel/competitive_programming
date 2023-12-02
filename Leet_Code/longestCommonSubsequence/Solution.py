class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1, l2 = len(text1), len(text2)
        dp_matrix = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if (text1[i - 1] == text2[j - 1]):
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                else:
                    dp_matrix[i][j] = max(dp_matrix[i-1][j], dp_matrix[i][j-1])
        return dp_matrix[l1][l2]