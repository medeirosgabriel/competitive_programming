def longestPalindromic(s):
    n = len(s)
    if (n <= 1): return s
    max_len, max_str = 1, s[0]
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
        for j in range(i):
            if (s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1])):
                dp[i][j] = True
                if (i - j + 1 > max_len):
                    max_len = i - j + 1
                    max_str = s[j:i+1]
    return max_str

print(longestPalindromic("taqsannasgh"))