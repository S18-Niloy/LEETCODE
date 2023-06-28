import math

class Solution:
    def numSquares(self, n):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            sqrt_i = int(math.sqrt(i))
            for j in range(1, sqrt_i + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        
        return dp[n]
