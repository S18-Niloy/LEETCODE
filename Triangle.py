class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Get the number of rows in the triangle
        n = len(triangle)

        # Create a DP table to store the minimum path sum at each position
        dp = triangle[-1]  # Start with the bottom row

        # Iterate from the second-to-last row up to the top row
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                # Calculate the minimum path sum at the current position
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        # The minimum path sum will be stored at dp[0]
        return dp[0]
