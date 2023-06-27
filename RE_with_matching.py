class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D DP table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: an empty pattern matches an empty string
        dp[0][0] = True
        
        # Handling patterns like a*, a*b*, a*b*c*, etc. (matches zero characters)
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # Matches zero preceding element
                    
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]  # Matches one or more preceding element
        
        return dp[len(s)][len(p)]
