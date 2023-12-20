from sys import maxint

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = -maxint - 1
        max_here = 0
        for i in range(len(nums)):
            max_here += nums[i]
            if (max_here > max_):
                max_ = max_here
            if (max_here < 0):
                max_here = 0
        return max_
