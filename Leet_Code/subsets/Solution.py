class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self. result = []
        self.backtracking(nums, [])
        return self.result

    def backtracking(self, subset, curr):
        self.result.append(curr)
        if (subset):
            for i in range(len(subset)):
                n = subset[i]
                self.backtracking(
                    subset[i + 1:], 
                    [n] + curr
                )
                
