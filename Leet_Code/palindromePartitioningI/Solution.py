# Backtracking
class Solution(object):
    
    def isPalindrome(self, s, l, r):
        while (l <= r):
            if (s[l] != s[r]):
                return False
            l, r = l + 1, r - 1
        return True

    def dfs(self, i, s, result, part):
        if (i >= len(s)):
            result.append(list(part))
            return
        for j in range(i, len(s)):
            if (self.isPalindrome(s, i, j)):
                part.append(s[i:j + 1])
                self.dfs(j + 1, s, result, part)
                part.pop()
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result, part = [], []
        self.dfs(0, s, result, part)
        return result
        
