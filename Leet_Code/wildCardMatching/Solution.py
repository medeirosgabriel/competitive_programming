class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        cache={}
        def dfs(i, j):
            if (i,j) in cache: return cache[i,j]
            if i >= len(s) and j >= len(p):
                cache[(i,j)] = True
                return cache[(i,j)]
            if j >= len(p):
                cache[(i,j)] = False
                return cache[i,j]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '?' or p[j] == '*')
            
            if p[j] == '*':
                cache[(i,j)] = dfs(i, j + 1) or (match and dfs(i + 1, j))
                return cache[(i,j)]
            elif match:
                cache[(i,j)] = dfs(i + 1, j + 1)
                return cache[(i,j)]
            else:
                cache[(i,j)] = False
        
        return dfs(0, 0)
