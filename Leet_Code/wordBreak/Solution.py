class Solution(object):
    def dfs(self, s):
        if s in self.memory: return self.memory[s]
        if s in self.wordDict: return True
        for i in range(1, len(s)):
            if s[:i] in self.wordDict and self.dfs(s[i:]):
                self.memory[s] = True
                return True
        self.memory[s] = False
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.memory = {}
        self.wordDict = set(wordDict)
        return self.dfs(s)
