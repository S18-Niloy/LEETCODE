class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 0 or n == 1:
            return 1
        
        # Create a DP table to store the number of ways to climb to each step
        dp = [0] * (n + 1)
        
        # Base cases: there's only one way to reach the first and second steps
        dp[0] = dp[1] = 1
        
        # Fill the DP table iteratively
        for i in range(2, n + 1):
            # The number of ways to reach the current step is the sum of the
            # number of ways to reach the previous two steps
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
