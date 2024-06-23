class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if (obstacleGrid[m - 1][n - 1] == 1):
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0):
                    dp[i][j] = 1
                else:
                    if (j - 1 >= 0 and obstacleGrid[i][j - 1] == 0):
                        dp[i][j] += dp[i][j - 1]
                    if (i - 1 >= 0 and obstacleGrid[i - 1][j] == 0):
                        dp[i][j] += dp[i - 1][j]
        return dp[m - 1][n - 1]
