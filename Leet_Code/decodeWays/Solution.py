class Solution(object):
    def isOk(self, number):
        return (number[0] == '1') or \
                (number[0] == '2' and number[1] in '0123456')

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s[0] == '0'): return 0
        n = len(s)
        dp = {n: 1}
        for i in range(n - 1, -1, -1):
            if (s[i] == '0'):
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if (i + 2 <= n and self.isOk(s[i:i + 2])):
                dp[i] += dp[i + 2]
        return dp[0]
