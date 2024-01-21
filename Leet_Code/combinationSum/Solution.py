class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.backTracking([], candidates, target)
        return self.result

    def backTracking(self, curr, candidates, target):
        if (target == 0):
            self.result.append(curr)
        else:
            for i in range(len(candidates)):
                e = candidates[i]
                if (e <= target):
                    self.backTracking(curr + [e], candidates[i:], target - e)
