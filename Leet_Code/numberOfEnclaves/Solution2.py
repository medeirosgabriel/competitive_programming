from collections import deque

class Solution(object):

    def walk_off(self, i, j):
        return i - 1 < 0 or i + 1 >= self.n or j - 1 < 0 or j + 1 >= self.m

    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        q = deque()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for i in range(n):
            if grid[i][0] == 1:
                q.append((i, 0))
                grid[i][0] = 0
            if grid[i][m - 1] == 1:
                q.append((i, m - 1))
                grid[i][m - 1] = 0
        
        for j in range(m):
            if grid[0][j] == 1:
                q.append((0, j))
                grid[0][j] = 0
            if grid[n - 1][j] == 1:
                q.append((n - 1, j))
                grid[n - 1][j] = 0
        
        while q:
            i, j = q.popleft()
            for dr, dc in directions:
                if 0 <= i + dr < n and 0 <= j + dc < m and grid[i + dr][j + dc] == 1:
                    grid[i + dr][j + dc] = 0
                    q.append((i + dr, j + dc))
        
        return sum([cell for row in grid for cell in row])





            
            
