class Solution(object):
    def dfs(self, idx, tgt, path):
            if tgt < 0: return
            if tgt == 0:
                self.res.append(path)
                return
            for i in range(idx, len(self.candidates)):
                c = self.candidates[i]
                if c > tgt: break
                if i > idx and c == self.candidates[i-1]:
                    continue
                self.dfs(i + 1, tgt - c, path + [c])

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.candidates = candidates
        self.dfs(0, target, [])
        return self.res
