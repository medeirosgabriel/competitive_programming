class Solution(object):

    def longestSubstring(self, s, k):
        x = self.recursion(s,k)
        if x >= k: return x
        else: return 0
    
    def recursion(self, s, k):
        if (len(s) <= 1): return len(s)
        flag = True
        for i in range(len(s)):
            if (s.count(s[i]) < k):
                flag = False
                break
        if (flag): return len(s)
        left = self.recursion(s[:i], k)
        right = self.recursion(s[i + 1:], k)
        return left if (left > right) else right
