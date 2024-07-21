class Solution(object):

    def backtracking(self, curr, l):
        if (len(curr) == self.k):
            self.result.append(curr)
            return
        for i in range(len(l)):
            self.backtracking(curr + [l[i]], l[i + 1:])

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l = list(range(1, n + 1))
        self.k = k
        self.result = []
        self.backtracking([], l)
        return self.result
