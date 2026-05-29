class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if (n < 3): return 0
        p1, seq_diff, count = 0, nums[0] - nums[1], 0
        for p2 in range(n):
            diff = nums[p2 - 1] - nums[p2]
            if (diff == seq_diff and p2 - p1 + 1 >= 3):
                count += p2 - p1 - 1
            if (diff != seq_diff):
                seq_diff = diff
                p1 = p2 - 1
        return count
