class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a DP table to store the number of unique paths
        dp = [[0] * n for _ in range(m)]
        
        # Base cases: there's only one way to reach the cells in the first row and column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the DP table iteratively
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to reach the current cell is the sum
                # of the number of paths from the cell above and the cell to the left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
