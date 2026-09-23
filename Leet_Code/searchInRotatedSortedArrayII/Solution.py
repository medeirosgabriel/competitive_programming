class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int((l + r)/2)
            n = nums[mid]
            if n == target:
                return True
            while r > mid and nums[r] == nums[mid]:
                r -= 1
            if (nums[r] >= nums[mid]):
                if (nums[mid] < target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if (nums[l] <= target < nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
        return False
