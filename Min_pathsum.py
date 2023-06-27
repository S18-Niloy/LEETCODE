class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m = len(grid)
        n = len(grid[0])
        
        # Create a DP table to store the minimum sum at each cell
        dp = [[0] * n for _ in range(m)]
        
        # Fill the DP table iteratively
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    # Base case: the top-left cell
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    # Cells in the first row can only be reached from the left cell
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    # Cells in the first column can only be reached from the cell above
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    # Cells in other positions can be reached from either the cell above or the cell to the left
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[m - 1][n - 1]
