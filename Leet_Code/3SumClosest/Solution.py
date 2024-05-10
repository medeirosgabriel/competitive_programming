class Solution(object):
    def distance(self, x, y):
        if x >= y:
            result = x - y
        else:
            result = y - x
        return result
        
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closestSum = float('inf')
        diff = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                s = nums[i] + nums[left] + nums[right]
                dist = self.distance(s, target)
                if (dist < diff):
                    closestSum, diff = s, dist
                if (s < target):
                    left += 1
                else:
                    right -= 1

        return closestSum
