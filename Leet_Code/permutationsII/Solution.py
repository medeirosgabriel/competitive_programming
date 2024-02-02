from collections import Counter

class Solution(object):

    def backtracking(self, curr):
        if len(curr) == self.n:
            self.result.append(curr)
            return
        for key in self.counter:
            if self.counter[key]:
                self.counter[key] -= 1
                self.backtracking(curr + [key])    
                self.counter[key] += 1

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.counter = Counter(nums)
        self.n = len(nums)
        self.backtracking([])
        return self.result
