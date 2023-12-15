class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1:
            return s
        max_len = 1
        max_str = s[0]
        dp = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
            for j in range(i):
                if (s[i] == s[j] and (i - j <= 2 or dp[i - 1][j + 1])):
                    dp[i][j] = True
                    if (i - j + 1 > max_len):
                        max_len = i - j + 1
                        max_str = s[j:i+1]           
        return max_str

