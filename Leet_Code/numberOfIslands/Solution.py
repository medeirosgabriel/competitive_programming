class Solution(object):

    def isValid(self, grid, i, j):
        row = len(grid)
        column = len(grid[0])
        if (i >= 0 and j >= 0 and i < row and j < column):
            if (grid[i][j] == "1"):
                return True
        return False

    def dfsInGrid(self, grid, i, j):
        grid[i][j] = 0
        if (self.isValid(grid, i, j + 1)):
            self.dfsInGrid(grid, i, j + 1)

        if (self.isValid(grid, i, j - 1)):
            self.dfsInGrid(grid, i, j - 1)

        if (self.isValid(grid, i + 1, j)):
            self.dfsInGrid(grid, i + 1, j)

        if (self.isValid(grid, i - 1, j)):
            self.dfsInGrid(grid, i - 1, j)
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])

        land = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1"):
                    land.append([i,j])
        
        count = 0
        while (len(land) > 0):
            i, j = land.pop()
            if (grid[i][j] == "1"):
                count += 1
                self.dfsInGrid(grid, i, j)

        return count
