class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        resp = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                l = j + 1
                r = n - 1
                while (l < r):
                    if (nums[l] + nums[r] == target - nums[i] - nums[j]):
                        resp.append((nums[l], nums[r], nums[i], nums[j]))
                        l += 1
                        r -= 1
                    elif (nums[l] + nums[r] < target - nums[i] - nums[j]):
                        l += 1
                    else:
                        r -= 1
        return list(set(resp))
