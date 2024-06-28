class Solution(object):
    def backtracking(self, candidates, curr, sum_):
        if (sum_ == self.target):
            curr.sort()
            self.result.append(curr)
        else:
            for i in range(len(candidates)):
                c = candidates[i]
                if (i > 0 and candidates[i] == candidates[i - 1]):
                    continue
                elif (sum_ + c <= self.target):
                    self.backtracking(
                        candidates[i + 1:],
                        curr + [c],
                        sum_ + c
                    )

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.target, self.result = target, []
        self.backtracking(candidates, [], 0)
        return self.result
