class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        
        # Create a DP table to store the minimum number of insertions
        dp = [[0] * n for _ in range(n)]
        
        # Fill the DP table diagonally from bottom to top
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        
        return dp[0][n - 1]
