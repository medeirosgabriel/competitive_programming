class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.n = n
        def backtracking(count, queue):
            l = len(queue)
            if (l < self.n * 2):
                backtracking(count + 1, queue + ["("])
                if (count - 1 >= 0):
                    backtracking(count - 1, queue + [")"])
            else:
                if (count == 0):
                    self.result.append("".join(queue))

        backtracking(0, [])
        return self.result
