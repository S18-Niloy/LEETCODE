class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # Create a DP table to store the number of distinct subsequences
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the first row with 1's (empty string matches any t)
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the current characters match, add both cases:
                # - Take the current character and match the remaining substrings
                # - Skip the current character and match the entire t
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                # If the current characters don't match, skip the current character
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]
