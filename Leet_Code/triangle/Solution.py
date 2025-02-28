class Solution(object):
    def recursion(self, l, x, y, ans):
        if x >= len(l): return 0
        if (x,y) in self.memo: return self.memo[(x,y)]
        p1 = self.recursion(l, x + 1, y, ans)
        p2 = self.recursion(l, x + 1, y + 1, ans)
        ans += l[x][y] + min(p1, p2)
        self.memo[(x, y)] = ans
        return ans

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.memo = {}
        return self.recursion(triangle, 0, 0, 0)
