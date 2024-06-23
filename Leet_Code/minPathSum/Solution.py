class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                aux = []
                if (i - 1 >= 0):
                    aux.append(dp[i - 1][j])
                if (j - 1 >= 0):
                    aux.append(dp[i][j - 1])
                dp[i][j] = grid[i][j] + (min(aux) if aux else 0)
                print(i, j, dp[i][j])
        return dp[m - 1][n - 1]
