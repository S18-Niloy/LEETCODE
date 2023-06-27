class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m = len(grid)
        n = len(grid[0])
        
        # Create a DP table to store the number of unique paths
        dp = [[0] * n for _ in range(m)]
        
        # Base case: there's one way to reach the top-left cell if it's not an obstacle
        if grid[0][0] == 0:
            dp[0][0] = 1
        
        # Fill the DP table iteratively
        for i in range(m):
            for j in range(n):
                # Skip if the current cell is an obstacle
                if grid[i][j] == 1:
                    continue
                
                # Check the cells above and to the left
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        
        return dp[m - 1][n - 1]
