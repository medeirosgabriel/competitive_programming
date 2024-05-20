class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        def backtracking(curr, nums):
            self.result.append(curr)
            for i in range(len(nums)):
                if (i > 0 and nums[i - 1] == nums[i]):
                    continue
                backtracking(
                    curr + [nums[i]], 
                    nums[i + 1:]
                )
                
        nums.sort()
        backtracking([], nums)
        return self.result
