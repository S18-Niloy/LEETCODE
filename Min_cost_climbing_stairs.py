class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Create a DP table to store the minimum cost at each step
        dp = [0] * (len(cost) + 1)
        
        # Base cases: the minimum cost to reach the first and second steps is 0
        dp[0] = dp[1] = 0
        
        # Fill the DP table iteratively
        for i in range(2, len(cost) + 1):
            # The minimum cost to reach the current step is the minimum cost
            # of reaching the previous two steps, plus the cost of the current step
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[len(cost)]
