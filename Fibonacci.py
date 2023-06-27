class Solution:
    def fib(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Create a DP table to store the Fibonacci numbers
        dp = [0] * (n + 1)
        
        # Base cases: F(0) = 0, F(1) = 1
        dp[0] = 0
        dp[1] = 1
        
        # Fill the DP table iteratively
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
