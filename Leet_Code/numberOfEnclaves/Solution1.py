class Solution(object):

    def walk_off(self, i, j):
        return i - 1 < 0 or i + 1 >= self.n or j - 1 < 0 or j + 1 >= self.m
    
    def in_the_limit(self, i, j):
        return i >= 0 and i < self.n and j >= 0 and j < self.m

    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.n, self.m = len(grid), len(grid[0])
        self.visited = [[False for _ in range(self.m)] for _ in range(self.n)]
        self.flag = False
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                quantity = self.dfs(i, j)
                if not self.flag: count += quantity
                self.flag = False
        return count

    def dfs(self, i, j):
        if (self.in_the_limit(i, j) and not self.visited[i][j]):
            self.visited[i][j] = True
            if (self.grid[i][j] == 1):
                if (self.walk_off(i, j)): self.flag = True
                count = 1
                for dr, dc in self.directions:
                    count += self.dfs(i + dr, j + dc)
                return count
        return 0

            
            
