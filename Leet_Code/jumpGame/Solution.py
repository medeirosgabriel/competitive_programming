class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) == 1):
            return True
        
        m = 0
        last = len(nums) - 1
        for i in range(len(nums) - 1):
            n = nums[i]
            if (m == i + n and n == 0): 
                return False
            m = max(m, i + n)
            if (last <= m):
                return True
        return False
