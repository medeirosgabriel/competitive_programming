class Solution(object):

    def backtracking(self, result, curr, nums):
        if (len(curr) == self.size):
            result.append(curr)
        else:
            for i in range(len(nums)):
                self.backtracking(
                    result, 
                    curr + [nums[i]], 
                    nums[:i] + nums[i + 1:]
                )


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.size = len(nums)
        self.backtracking(result, [], nums)
        return result
        
