class Solution(object):
                
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # GREEDY
        out = 0
        r = l = 0
        while (r < len(nums) - 1):
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            out += 1
        return out
