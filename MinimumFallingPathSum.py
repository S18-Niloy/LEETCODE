class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # Create a DP table to store the minimum sum at each position
        dp = [[0] * n for _ in range(n)]
        
        # Copy the first row as the initial values of the DP table
        dp[0] = matrix[0]
        
        # Iterate from the second row up to the last row
        for i in range(1, n):
            for j in range(n):
                # Calculate the minimum sum at the current position
                dp[i][j] = matrix[i][j] + min(
                    dp[i - 1][j - 1] if j - 1 >= 0 else float('inf'),
                    dp[i - 1][j],
                    dp[i - 1][j + 1] if j + 1 < n else float('inf')
                )
        
        # The minimum sum will be the minimum value in the last row of the DP table
        return min(dp[-1])
