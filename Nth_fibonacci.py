class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # Create a DP table to store the Tribonacci numbers
        dp = [0] * (n + 1)
        
        # Base cases: T0 = 0, T1 = 1, T2 = 1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        # Fill the DP table iteratively
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]
