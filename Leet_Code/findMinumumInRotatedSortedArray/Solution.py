class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = self.findPoint(0, len(nums) - 1, nums)
        return nums[p]

    
    def findPoint(self, left, right, nums):
        if (left < right):
            mid = (left + right)/2
            n = nums[mid]
            if (n > nums[right]):
                return self.findPoint(mid + 1, right, nums)
            else:
                return self.findPoint(left, mid, nums)
        else:
            return left
