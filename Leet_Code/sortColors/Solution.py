class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            n = nums[i]
            ni = i
            for j in range(i + 1, len(nums)):
                if (nums[j] < n):
                    ni = j
                    n = nums[j]
            nums[i], nums[ni] = n, nums[i]
        return nums
