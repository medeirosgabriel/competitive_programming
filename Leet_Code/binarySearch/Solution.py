class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n - 1
        while (left <= right):
            mid = (left + right)/2
            if (nums[mid] == target):
                return mid
            elif (target < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
