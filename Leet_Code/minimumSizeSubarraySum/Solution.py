class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, curr_sum, ans = 0, 0, n + 1
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                ans = min(r - l  + 1, ans)
                curr_sum -= nums[l]
                l += 1
        return ans if ans != n + 1 else 0
